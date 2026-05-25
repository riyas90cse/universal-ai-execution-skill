# Symphony-Style Workflow Adapter

Use this adapter for issue-driven orchestration in environments that coordinate
multiple steps or agents. It is a workflow instruction document only; it does
not provide a Symphony runtime or native integration.

## Canonical Sources

- Router: `skills/universal-ai-execution/SKILL.md`
- Workflow registry: `skills/universal-ai-execution/references/workflow-registry.yaml`
- Optional focused skill mappings: `focused_skill_mappings` in the workflow registry
- Task classification: `skills/universal-ai-execution/references/task-classification-rules.md`
- Output contracts: `skills/universal-ai-execution/references/output-contracts.md`
- Validation matrix: `skills/universal-ai-execution/references/validation-matrix.md`
- PR breakdown rules: `skills/universal-ai-execution/references/pr-breakdown-rules.md`
- Anti-pattern rules: `skills/universal-ai-execution/references/anti-patterns.md`

Do not duplicate workflows inside this adapter.

## Issue-Driven Orchestration

1. Read the issue, user request, and repository instructions.
2. Read `skills/universal-ai-execution/SKILL.md`.
3. Classify the task using the canonical classification rules.
4. Select the workflow from the canonical registry.
5. Read a mapped focused skill when one exists and helps the selected workflow.
6. Inventory relevant files, docs, tests, configs, and source-of-truth material.
7. Plan the smallest reviewable change.
8. Implement only the current issue scope.
9. Validate using the validation matrix and workflow-specific requirements.
10. Report changed files, validation performed, known risks, and remaining
   out-of-scope work.

## Small PR Discipline

- Keep each implementation pass tied to one issue or review purpose.
- Split unrelated concerns by using the PR breakdown rules.
- Do not combine refactors, behavior changes, generated churn, and docs cleanup
  unless the issue explicitly requires it.
- Preserve existing architecture and conventions.

## Stop Conditions

Stop and ask for clarification, approval, or a narrower scope when any condition
below applies:

- Large deletes are required or proposed.
- Requirements conflict with each other.
- Security-sensitive behavior is ambiguous.
- Database migration, rollback, or data preservation risk is unclear.
- Product behavior or acceptance criteria are ambiguous.
- Required source-of-truth documents or files are missing.
- Acceptance criteria are unclear or cannot be validated.
- The requested work would require a new runtime, CLI, adapter framework, or
  native integration not already in scope.

## Report Format

Report:

- Selected workflow and execution mode.
- Files inventoried.
- Plan or implementation summary.
- Validation performed and results.
- Stop conditions encountered, if any.
- Compatibility limitation: this adapter is orchestration guidance only.
