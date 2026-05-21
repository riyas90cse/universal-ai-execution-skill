# GitHub Copilot Adapter

Use the Universal AI Execution Skill for scoped software work.

Canonical router:

`skills/universal-ai-execution/SKILL.md`

Canonical references:

- Workflow registry: `skills/universal-ai-execution/references/workflow-registry.yaml`
- Task classification: `skills/universal-ai-execution/references/task-classification-rules.md`
- Output contracts: `skills/universal-ai-execution/references/output-contracts.md`
- Validation rules: `skills/universal-ai-execution/references/validation-matrix.md`
- Anti-pattern rules: `skills/universal-ai-execution/references/anti-patterns.md`

Before responding:

1. Classify the task.
2. Select the workflow from the registry.
3. Inspect relevant repository files before implementation.
4. Keep the change small and reviewable.
5. Preserve existing architecture and conventions.
6. Apply the matching output contract.
7. Validate before claiming completion.

Prefer small PRs. Do not copy the workflow registry into this file. This adapter
is instruction text only and depends on the Copilot environment honoring
repository or chat instructions.
