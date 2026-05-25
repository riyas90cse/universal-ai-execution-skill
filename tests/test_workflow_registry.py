from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "skills/universal-ai-execution/references/workflow-registry.yaml"
FIXTURE_PATH = ROOT / "tests/fixtures/required_workflow_ids.txt"
EXPECTED_WORKFLOW_COUNT = 46
REQUIRED_FOCUSED_SKILL_PATHS = {
    "skills/setup-universal-ai-execution/SKILL.md",
    "skills/productivity/write-a-skill/SKILL.md",
    "skills/productivity/grill-me/SKILL.md",
    "skills/engineering/review-changes/SKILL.md",
    "skills/engineering/full-codebase-audit/SKILL.md",
    "skills/engineering/refactor-plan/SKILL.md",
    "skills/security/security-audit/SKILL.md",
}

REQUIRED_WORKFLOW_FIELDS = (
    "id",
    "name",
    "category",
    "when_to_use",
    "workflow_sequence",
    "focus_areas",
    "required_outputs",
    "validation_rules",
    "common_mistakes",
)

REQUIRED_LIST_FIELDS = (
    "workflow_sequence",
    "focus_areas",
    "required_outputs",
    "validation_rules",
    "common_mistakes",
)


def load_registry() -> dict:
    with REGISTRY_PATH.open("r", encoding="utf-8") as registry_file:
        return yaml.safe_load(registry_file)


def required_workflow_ids() -> list[str]:
    return [
        line.strip()
        for line in FIXTURE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def registry_workflows() -> list[dict]:
    return load_registry()["workflows"]


def test_workflow_registry_exists() -> None:
    assert REGISTRY_PATH.is_file()


def test_required_workflow_fixture_has_46_unique_ids() -> None:
    ids = required_workflow_ids()

    assert len(ids) == EXPECTED_WORKFLOW_COUNT
    assert len(set(ids)) == EXPECTED_WORKFLOW_COUNT


def test_registry_declared_count_matches_workflows() -> None:
    registry = load_registry()
    workflows = registry["workflows"]

    assert registry["workflow_count"] == EXPECTED_WORKFLOW_COUNT
    assert len(workflows) == EXPECTED_WORKFLOW_COUNT
    assert registry["workflow_count"] == len(workflows)


def test_registry_contains_exact_required_workflow_ids() -> None:
    actual_ids = {workflow["id"] for workflow in registry_workflows()}
    expected_ids = set(required_workflow_ids())

    assert actual_ids == expected_ids


def test_registry_workflow_ids_are_unique() -> None:
    ids = [workflow["id"] for workflow in registry_workflows()]

    assert len(ids) == len(set(ids))


def test_registry_workflows_have_required_structure() -> None:
    for workflow in registry_workflows():
        for field in REQUIRED_WORKFLOW_FIELDS:
            assert field in workflow, f"{workflow.get('id', '<missing id>')} missing {field}"

        for field in ("id", "name", "category", "when_to_use"):
            assert isinstance(workflow[field], str)
            assert workflow[field].strip()

        for field in REQUIRED_LIST_FIELDS:
            assert isinstance(workflow[field], list)
            assert workflow[field]
            assert all(isinstance(item, str) and item.strip() for item in workflow[field])


def test_focused_skill_mappings_reference_existing_workflows_and_files() -> None:
    registry = load_registry()
    workflow_ids = {workflow["id"] for workflow in registry_workflows()}
    mappings = registry["focused_skill_mappings"]

    assert isinstance(mappings, dict)
    assert mappings
    assert REQUIRED_FOCUSED_SKILL_PATHS.issubset(set(mappings.values()))

    for workflow_id, focused_path in mappings.items():
        assert workflow_id in workflow_ids
        assert isinstance(focused_path, str)
        assert focused_path.strip()
        assert (ROOT / focused_path).is_file(), focused_path
