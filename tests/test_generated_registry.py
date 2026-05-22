from __future__ import annotations

from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "skills/universal-ai-execution/references/workflow-registry.yaml"
TECHNIQUE_REGISTRY_PATH = ROOT / "skills/universal-ai-execution/references/technique-registry.md"
FIXTURE_PATH = ROOT / "tests/fixtures/required_workflow_ids.txt"
EXPECTED_WORKFLOW_COUNT = 46


def required_workflow_ids() -> set[str]:
    return {
        line.strip()
        for line in FIXTURE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def registry_workflow_ids() -> set[str]:
    with REGISTRY_PATH.open("r", encoding="utf-8") as registry_file:
        registry = yaml.safe_load(registry_file)

    return {workflow["id"] for workflow in registry["workflows"]}


def generated_workflow_ids() -> set[str]:
    content = TECHNIQUE_REGISTRY_PATH.read_text(encoding="utf-8")
    return set(re.findall(r"^### `([^`]+)`$", content, flags=re.MULTILINE))


def test_generated_registry_exists() -> None:
    assert TECHNIQUE_REGISTRY_PATH.is_file()


def test_generated_registry_declares_source_and_router() -> None:
    content = TECHNIQUE_REGISTRY_PATH.read_text(encoding="utf-8")

    assert "Generated from `workflow-registry.yaml`" in content
    assert "- Workflow count: 46" in content
    assert "- Source of truth: `skills/universal-ai-execution/references/workflow-registry.yaml`" in content
    assert "- Router: `skills/universal-ai-execution/SKILL.md`" in content


def test_generated_registry_contains_all_required_workflows() -> None:
    ids = generated_workflow_ids()

    assert len(ids) == EXPECTED_WORKFLOW_COUNT
    assert ids == required_workflow_ids()


def test_generated_registry_matches_yaml_registry_ids() -> None:
    assert generated_workflow_ids() == registry_workflow_ids()
