# Focused Skill Template

Use this template when adding a focused skill that accelerates one or more existing Universal AI Execution workflow IDs.

Focused skills must not redefine workflows. Keep workflow selection in the router and workflow definitions in `../references/workflow-registry.yaml`.

```markdown
---
name: focused-skill-name
description: One sentence explaining the focused execution playbook.
---

# Focused Skill Name

## Purpose

State what deeper execution help this skill provides after the router has selected a workflow.

## Mapped Workflows

- `existing-workflow-id`

## When To Use

- Name the user signals or task shapes that benefit from this focused playbook.

## Required Inputs

- Name the minimum information needed to use the skill safely.

## Process

1. Start with inventory or task understanding.
2. Apply focused execution steps without expanding scope.
3. Validate before claiming completion.

## Output Contract

Describe the output sections this focused skill should produce. Reference `../references/output-contracts.md` when the canonical output contract is sufficient.

## Validation Checklist

- Confirm every mapped workflow ID exists in the registry.
- Confirm the focused skill did not duplicate registry workflow content.
- Confirm the output follows the selected contract.

## Common Mistakes

- Using the focused skill as a router replacement.
- Copying registry workflow definitions into this file.
- Adding new workflow IDs without a registry issue.
```
