# Claude Code Adapter

Use this file as a Claude Code `CLAUDE.md` project instruction file when you
want Claude Code to apply the Universal AI Execution Skill in a repository.

## How Claude Code Uses This File

Claude Code can use `CLAUDE.md` files as project instructions. Place this
adapter at the repository root as `CLAUDE.md`, or merge its instructions into an
existing project `CLAUDE.md` file.

If another `CLAUDE.md` file already exists, preserve its repository-specific
instructions and add only the routing instructions below.

## Skill Location

The canonical skill lives at:

`skills/universal-ai-execution/SKILL.md`

`SKILL.md` is the router. It tells Claude Code to:

- Understand and classify the task.
- Select a workflow from Workflow Registry v1.
- Apply the matching output contract.
- Validate before claiming completion.

Workflow Registry v1 lives at:

`skills/universal-ai-execution/references/workflow-registry.yaml`

Output contracts live at:

`skills/universal-ai-execution/references/output-contracts.md`

Guardrail references live under:

`skills/universal-ai-execution/references/`

## Claude Code Instruction

Before planning, editing, reviewing, or validating work, read
`skills/universal-ai-execution/SKILL.md`.

Then:

1. Classify the task using the skill references.
2. Select the workflow from `references/workflow-registry.yaml`.
3. Apply the output contract from `references/output-contracts.md`.
4. Follow the guardrail references for validation, PR breakdown, security,
   documentation, product/business review, and anti-pattern checks.
5. Inventory relevant files before implementation.
6. Keep changes scoped to the current issue or user request.
7. Validate before claiming completion.

Do not copy workflow definitions into this adapter. Treat the skill files as the
source of truth.

This adapter is Claude Code project-instruction guidance. It does not provide a
runtime integration or guarantee that Claude Code can read files outside the
context and tool permissions available in the current session.
