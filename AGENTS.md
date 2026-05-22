# Agent Instructions

Agents must use the Universal AI Execution Skill at:

`skills/universal-ai-execution/SKILL.md`

## Required Behavior

- Read the repository before editing.
- Follow only the current issue scope.
- Keep changes small, structured, and reviewable.
- Do not merge unrelated concerns across files.
- Preserve the router, registry, reference, adapter, example, and test boundaries.
- Validate before claiming completion.

## Source of Truth

- Router: `skills/universal-ai-execution/SKILL.md`
- Workflow Registry v1: `skills/universal-ai-execution/references/workflow-registry.yaml`
- Generated registry: `skills/universal-ai-execution/references/technique-registry.md`
- Output contracts: `skills/universal-ai-execution/references/output-contracts.md`
- Structure validation: `tests/` and `scripts/validate-skill-structure.py`

Do not duplicate workflow registry content into router, adapter, example, or README files.
