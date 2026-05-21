# Codex Adapter

Use this file as a Codex `AGENTS.md` instruction file when you want Codex to
apply the Universal AI Execution Skill in a repository.

## How Codex Uses This File

Codex reads `AGENTS.md` files as repository instructions. Place this adapter at
the repository root or merge its instructions into an existing `AGENTS.md` file.

If another `AGENTS.md` file already exists, preserve its repository-specific
instructions and add only the routing instructions below.

## Skill Location

The canonical skill lives at:

`skills/universal-ai-execution/SKILL.md`

`SKILL.md` is the router. It tells Codex to:

- Understand and classify the task.
- Select a workflow from the registry.
- Apply the matching output contract.
- Validate before claiming completion.

The workflow registry lives at:

`skills/universal-ai-execution/references/workflow-registry.yaml`

Detailed output contracts live at:

`skills/universal-ai-execution/references/output-contracts.md`

## Codex Instruction

Before planning, editing, reviewing, or validating work, read
`skills/universal-ai-execution/SKILL.md`.

Then:

1. Classify the task using the skill references.
2. Select the workflow from `references/workflow-registry.yaml`.
3. Apply the output contract from `references/output-contracts.md`.
4. Follow the guardrail references for validation, PR breakdown, security,
   documentation, and anti-pattern checks.
5. Keep changes scoped to the current issue or user request.
6. Validate before claiming completion.

Do not copy workflow definitions into this adapter. Treat the skill files as the
source of truth.
