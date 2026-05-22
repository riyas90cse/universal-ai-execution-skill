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
    "AGENTS.md",
    "WORKFLOW.md",
    "skills/universal-ai-execution/SKILL.md",
    "skills/universal-ai-execution/references/workflow-registry.yaml",
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

ROUTER_FORBIDDEN_REGISTRY_MARKERS = (
    "workflow_count:",
    "workflows:",
    "workflow_sequence:",
    "required_outputs:",
    "validation_rules:",
    "common_mistakes:",
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
    front_matter_end = skill_content.find("\n---\n", 4)
    if not skill_content.startswith("---\n") or front_matter_end == -1:
        errors.append("SKILL.md must have YAML front matter.")
    else:
        front_matter = skill_content[4:front_matter_end]
        if "name:" not in front_matter:
            errors.append("SKILL.md front matter must include name.")
        if "description:" not in front_matter:
            errors.append("SKILL.md front matter must include description.")

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
