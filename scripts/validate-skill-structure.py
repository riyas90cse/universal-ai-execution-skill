#!/usr/bin/env python3
"""Validate Universal AI Execution Skill package structure."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Any

try:
    import yaml
except ModuleNotFoundError as exc:  # pragma: no cover - dependency guard
    raise SystemExit(
        "PyYAML is required for structure validation. "
        "Install dev requirements with: python -m pip install -r requirements-dev.txt"
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "skills/universal-ai-execution/SKILL.md"
REGISTRY_PATH = ROOT / "skills/universal-ai-execution/references/workflow-registry.yaml"
TECHNIQUE_REGISTRY_PATH = ROOT / "skills/universal-ai-execution/references/technique-registry.md"
FIXTURE_PATH = ROOT / "tests/fixtures/required_workflow_ids.txt"
EXPECTED_WORKFLOW_COUNT = 46

REQUIRED_PATHS = (
    ".github/workflows/ci.yml",
    "AGENTS.md",
    "WORKFLOW.md",
    "docs/focused-skills.md",
    "examples/requirements-driven-prompting-example.md",
    "examples/focused-code-review-example.md",
    "examples/focused-security-audit-example.md",
    "skills/universal-ai-execution/templates/focused-skill-template.md",
    "skills/universal-ai-execution/SKILL.md",
    "skills/universal-ai-execution/references/workflow-registry.yaml",
    "skills/universal-ai-execution/references/workflow-registry.schema.json",
    "skills/universal-ai-execution/references/technique-registry.md",
    "skills/universal-ai-execution/references/task-classification-rules.md",
    "skills/universal-ai-execution/references/output-contracts.md",
    "skills/universal-ai-execution/references/validation-matrix.md",
    "skills/universal-ai-execution/references/pr-breakdown-rules.md",
    "skills/universal-ai-execution/references/anti-patterns.md",
    "skills/universal-ai-execution/references/security-review-rules.md",
    "skills/universal-ai-execution/references/documentation-review-rules.md",
    "skills/universal-ai-execution/references/product-business-review-rules.md",
    "adapters/codex/AGENTS.md",
    "adapters/claude-code/CLAUDE.md",
    "adapters/cursor/universal-ai-execution.mdc",
    "adapters/github-copilot/copilot-instructions.md",
    "adapters/generic-llm/universal-invocation-prompt.md",
    "adapters/symphony/WORKFLOW.md",
)

REQUIRED_FOCUSED_SKILL_PATHS = (
    "skills/setup-universal-ai-execution/SKILL.md",
    "skills/productivity/write-a-skill/SKILL.md",
    "skills/productivity/grill-me/SKILL.md",
    "skills/engineering/review-changes/SKILL.md",
    "skills/engineering/full-codebase-audit/SKILL.md",
    "skills/engineering/refactor-plan/SKILL.md",
    "skills/security/security-audit/SKILL.md",
)

REQUIRED_FOCUSED_SKILL_SECTIONS = (
    "## Purpose",
    "## Mapped Workflows",
    "## When To Use",
    "## Required Inputs",
    "## Process",
    "## Output Contract",
    "## Validation Checklist",
    "## Common Mistakes",
)

ROUTER_FORBIDDEN_REGISTRY_MARKERS = (
    "workflow_count:",
    "workflows:",
    "workflow_sequence:",
    "required_outputs:",
    "validation_rules:",
    "common_mistakes:",
)


REGISTRY_DUPLICATION_SCAN_ROOTS = (
    "adapters",
    "examples",
)

REGISTRY_DUPLICATION_SCAN_FILES = (
    "README.md",
    "docs/focused-skills.md",
)


def required_workflow_ids() -> list[str]:
    return [
        line.strip()
        for line in FIXTURE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_registry() -> dict[str, Any]:
    with REGISTRY_PATH.open("r", encoding="utf-8") as registry_file:
        registry = yaml.safe_load(registry_file)

    if not isinstance(registry, dict):
        raise ValueError("workflow-registry.yaml must contain a mapping.")

    return registry


def registry_duplicate_fragments(registry: dict[str, Any]) -> list[tuple[str, str, str]]:
    fragments: list[tuple[str, str, str]] = []

    for workflow in registry.get("workflows", []):
        if not isinstance(workflow, dict):
            continue

        workflow_id = str(workflow.get("id", "<unknown>"))

        sequence = workflow.get("workflow_sequence")
        if isinstance(sequence, list) and all(isinstance(item, str) for item in sequence):
            fragments.append((workflow_id, "workflow_sequence", " → ".join(sequence)))

        for field in ("required_outputs", "validation_rules", "common_mistakes"):
            items = workflow.get(field)
            if isinstance(items, list) and len(items) > 1 and all(isinstance(item, str) for item in items):
                fragments.append((workflow_id, field, "\n".join(f"- {item}" for item in items)))

    return fragments


def duplication_scan_paths() -> list[Path]:
    paths = [ROOT / path for path in REGISTRY_DUPLICATION_SCAN_FILES]
    paths.extend(ROOT / path for path in REQUIRED_FOCUSED_SKILL_PATHS)
    paths.append(ROOT / "skills/universal-ai-execution/templates/focused-skill-template.md")

    for root in REGISTRY_DUPLICATION_SCAN_ROOTS:
        paths.extend((ROOT / root).rglob("*.md"))

    return sorted({path for path in paths if path.is_file()})


def validate_skill_front_matter(content: str, path: str, errors: list[str]) -> None:
    front_matter_end = content.find("\n---\n", 4)
    if not content.startswith("---\n") or front_matter_end == -1:
        errors.append(f"{path} must have YAML front matter.")
        return

    front_matter = content[4:front_matter_end]
    if "name:" not in front_matter:
        errors.append(f"{path} front matter must include name.")
    if "description:" not in front_matter:
        errors.append(f"{path} front matter must include description.")


def validate() -> list[str]:
    errors: list[str] = []

    for path in REQUIRED_PATHS:
        if not (ROOT / path).is_file():
            errors.append(f"Missing required file: {path}")

    if not FIXTURE_PATH.is_file():
        errors.append(f"Missing required fixture: {FIXTURE_PATH.relative_to(ROOT)}")
        return errors

    if not SKILL_PATH.is_file() or not REGISTRY_PATH.is_file() or not TECHNIQUE_REGISTRY_PATH.is_file():
        return errors

    skill_content = SKILL_PATH.read_text(encoding="utf-8")
    validate_skill_front_matter(skill_content, "SKILL.md", errors)

    for marker in ROUTER_FORBIDDEN_REGISTRY_MARKERS:
        if marker in skill_content:
            errors.append(f"SKILL.md must not duplicate registry marker: {marker}")

    expected_ids = set(required_workflow_ids())
    for workflow_id in expected_ids:
        if workflow_id in skill_content:
            errors.append(f"SKILL.md must not duplicate workflow ID: {workflow_id}")

    if len(expected_ids) != EXPECTED_WORKFLOW_COUNT:
        errors.append(f"required_workflow_ids.txt must contain {EXPECTED_WORKFLOW_COUNT} unique IDs.")

    registry = load_registry()
    workflows = registry.get("workflows")
    if not isinstance(workflows, list):
        errors.append("workflow-registry.yaml field 'workflows' must be a list.")
        workflows = []

    actual_ids = [workflow.get("id") for workflow in workflows if isinstance(workflow, dict)]
    if registry.get("workflow_count") != EXPECTED_WORKFLOW_COUNT:
        errors.append(f"workflow_count must be {EXPECTED_WORKFLOW_COUNT}.")
    if len(workflows) != EXPECTED_WORKFLOW_COUNT:
        errors.append(f"workflow-registry.yaml must contain {EXPECTED_WORKFLOW_COUNT} workflows.")
    if len(actual_ids) != len(set(actual_ids)):
        errors.append("workflow IDs must be unique.")
    if set(actual_ids) != expected_ids:
        missing = sorted(expected_ids - set(actual_ids))
        extra = sorted(set(actual_ids) - expected_ids)
        errors.append(f"workflow IDs must match fixture. Missing={missing}; extra={extra}")

    for path in duplication_scan_paths():
        content = path.read_text(encoding="utf-8")
        relative_path = path.relative_to(ROOT).as_posix()
        for workflow_id, field, fragment in registry_duplicate_fragments(registry):
            if fragment and fragment in content:
                errors.append(
                    f"{relative_path} must not duplicate registry {field} content for workflow {workflow_id}."
                )

    focused_skill_mappings = registry.get("focused_skill_mappings")
    if not isinstance(focused_skill_mappings, dict) or not focused_skill_mappings:
        errors.append("workflow-registry.yaml must define non-empty focused_skill_mappings.")
        focused_skill_mappings = {}

    required_focused_paths = set(REQUIRED_FOCUSED_SKILL_PATHS)
    mapped_focused_paths = set()
    for workflow_id, focused_path in focused_skill_mappings.items():
        if workflow_id not in set(actual_ids):
            errors.append(f"focused_skill_mappings references unknown workflow ID: {workflow_id}")
        if not isinstance(focused_path, str) or not focused_path.strip():
            errors.append(f"focused_skill_mappings value for {workflow_id} must be a non-empty path.")
            continue
        mapped_focused_paths.add(focused_path)
        if not (ROOT / focused_path).is_file():
            errors.append(f"focused_skill_mappings path does not exist: {focused_path}")

    missing_focused_paths = sorted(required_focused_paths - mapped_focused_paths)
    if missing_focused_paths:
        errors.append(f"Focused skills must map to at least one workflow ID: {missing_focused_paths}")

    for focused_path in REQUIRED_FOCUSED_SKILL_PATHS:
        full_path = ROOT / focused_path
        if not full_path.is_file():
            errors.append(f"Missing required focused skill: {focused_path}")
            continue

        focused_content = full_path.read_text(encoding="utf-8")
        validate_skill_front_matter(focused_content, focused_path, errors)
        for section in REQUIRED_FOCUSED_SKILL_SECTIONS:
            if section not in focused_content:
                errors.append(f"{focused_path} missing required section: {section}")
        for marker in ROUTER_FORBIDDEN_REGISTRY_MARKERS:
            if marker in focused_content:
                errors.append(f"{focused_path} must not duplicate registry marker: {marker}")

        mapped_workflow_ids = re.findall(r"^- `([^`]+)`$", focused_content, flags=re.MULTILINE)
        if not mapped_workflow_ids:
            errors.append(f"{focused_path} must map to at least one workflow ID.")
        for mapped_workflow_id in mapped_workflow_ids:
            if mapped_workflow_id not in set(actual_ids):
                errors.append(f"{focused_path} references unknown workflow ID: {mapped_workflow_id}")
            if focused_skill_mappings.get(mapped_workflow_id) != focused_path:
                errors.append(
                    f"{focused_path} mapped workflow {mapped_workflow_id} must match focused_skill_mappings."
                )

    technique_content = TECHNIQUE_REGISTRY_PATH.read_text(encoding="utf-8")
    generated_ids = set(re.findall(r"^### `([^`]+)`$", technique_content, flags=re.MULTILINE))
    if generated_ids != expected_ids:
        missing = sorted(expected_ids - generated_ids)
        extra = sorted(generated_ids - expected_ids)
        errors.append(f"technique registry IDs must match fixture. Missing={missing}; extra={extra}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Skill structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
