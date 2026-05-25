---
name: write-a-skill
description: Write or refine focused skills that extend the universal router without copying the workflow registry.
---

# Write A Skill

## Purpose

Use this focused skill to create or improve a focused skill playbook that sits beside the Universal AI Execution router. The result should provide deeper execution guidance for selected workflows while leaving workflow selection and canonical workflow definitions in the registry.

## Mapped Workflows

- `documentation-cleanup`

## When To Use

- A new focused skill needs to be created for one or more existing workflow IDs.
- An existing focused skill needs clearer inputs, process, validation, or output expectations.
- Skill documentation needs to be checked for duplication against the registry.
- The request is about improving skill usability, not adding workflow IDs.

## Required Inputs

- Focused skill name and intended path.
- Existing workflow IDs it accelerates.
- User task or issue that justifies the focused skill.
- Any platform or adapter constraints.

## Process

1. Confirm every mapped workflow ID already exists in the workflow registry.
2. Define the skill purpose as an execution accelerator, not a router replacement.
3. Write concrete usage guidance for inputs, process, output, validation, and mistakes.
4. Keep registry-owned details out of the skill body except the mapped workflow IDs.
5. Prefer short checklists and practical playbooks over broad theory.
6. Validate required sections, front matter, and mapping references.

## Output Contract

Return a skill authoring summary with:

- Skill path and name.
- Mapped workflow IDs.
- New or updated sections.
- Registry duplication risks checked.
- Validation commands run and results.

## Validation Checklist

- The skill has YAML front matter with `name` and `description`.
- The skill includes all required focused-skill sections.
- Every mapped workflow ID exists in the workflow registry.
- The skill does not duplicate full workflow registry entries.
- The skill path is included in the focused skill mapping when applicable.

## Common Mistakes

- Creating a skill before confirming the workflow mapping.
- Copying full workflow sequences, outputs, and validation rules from the registry.
- Writing vague advice that cannot guide execution.
- Adding new workflow IDs as part of skill authoring.
