from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "skills/universal-ai-execution/SKILL.md"
FIXTURE_PATH = ROOT / "tests/fixtures/required_workflow_ids.txt"

REQUIRED_REFERENCE_FILES = (
    "workflow-registry.yaml",
    "technique-registry.md",
    "task-classification-rules.md",
    "output-contracts.md",
    "validation-matrix.md",
    "pr-breakdown-rules.md",
    "anti-patterns.md",
    "security-review-rules.md",
    "documentation-review-rules.md",
    "product-business-review-rules.md",
)

REQUIRED_ADAPTER_FILES = (
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


def read_skill() -> str:
    return SKILL_PATH.read_text(encoding="utf-8")


def required_workflow_ids() -> list[str]:
    return [
        line.strip()
        for line in FIXTURE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def test_skill_file_exists() -> None:
    assert SKILL_PATH.is_file()


def test_skill_has_yaml_front_matter_with_name_and_description() -> None:
    content = read_skill()

    assert content.startswith("---\n")
    end_marker = content.find("\n---\n", 4)
    assert end_marker != -1

    front_matter = content[4:end_marker]
    assert "name:" in front_matter
    assert "description:" in front_matter


def test_required_root_files_exist() -> None:
    assert (ROOT / "AGENTS.md").is_file()
    assert (ROOT / "WORKFLOW.md").is_file()


def test_required_reference_files_exist() -> None:
    references_root = ROOT / "skills/universal-ai-execution/references"

    for filename in REQUIRED_REFERENCE_FILES:
        assert (references_root / filename).is_file(), filename


def test_required_adapter_files_exist() -> None:
    for path in REQUIRED_ADAPTER_FILES:
        assert (ROOT / path).is_file(), path


def test_generic_invocation_prompt_exists() -> None:
    assert (ROOT / "adapters/generic-llm/universal-invocation-prompt.md").is_file()


def test_router_and_registry_content_stay_separate() -> None:
    content = read_skill()

    for marker in ROUTER_FORBIDDEN_REGISTRY_MARKERS:
        assert marker not in content

    for workflow_id in required_workflow_ids():
        assert workflow_id not in content

    assert "Router:" in content
    assert "Registry:" in content
