---
name: setup-universal-ai-execution
description: Configure the Universal AI Execution Skill in a repository or agent environment without duplicating the workflow registry.
---

# Setup Universal AI Execution

## Purpose

Use this focused skill to install, adapt, or verify Universal AI Execution Skill usage in a repository. It helps connect the canonical router, registry, adapters, and validation commands while preserving source-of-truth boundaries.

## Mapped Workflows

- `documentation-source-of-truth-cleanup`

## When To Use

- A repository needs Universal AI Execution Skill instructions added or reconciled.
- Agent instructions reference stale or conflicting workflow locations.
- Adapter, README, or setup docs need to point to the canonical router.
- The task is about packaging or wiring the skill, not changing workflow definitions.

## Required Inputs

- Target repository or package path.
- Existing agent instruction files, if any.
- Desired adapter or agent environment.
- Validation command expectations for the target repository.

## Process

1. Inventory existing agent instructions, README setup notes, adapters, and validation scripts.
2. Identify the canonical router and registry paths before editing.
3. Remove or update conflicting setup guidance that duplicates workflow content.
4. Add only the smallest adapter or documentation change needed to route agents to the canonical skill.
5. Preserve workflow definitions, output contracts, and generated registry ownership.
6. Validate links, paths, and structure after edits.

## Output Contract

Return a setup summary with:

- Files inspected.
- Files changed.
- Canonical router and registry paths.
- Adapter or instruction changes made.
- Validation commands run and results.
- Remaining setup gaps or follow-up tasks.

## Validation Checklist

- The canonical router remains `skills/universal-ai-execution/SKILL.md`.
- Workflow definitions remain in the workflow registry.
- No adapter or README duplicates full workflow definitions.
- Paths are relative, portable, and correct from the repository root.
- Validation commands were run, or the reason they were not run is stated.

## Common Mistakes

- Copying workflow definitions into setup docs.
- Treating an adapter as a new source of truth.
- Changing workflow IDs while fixing setup instructions.
- Adding broad repository policy changes beyond setup scope.
