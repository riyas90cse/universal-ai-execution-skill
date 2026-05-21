# Generic LLM Invocation Prompt

Copy and paste this prompt into an LLM environment that has no native skill
support. Provide the repository files or excerpts listed in `[REPO_CONTEXT]` so
the model can inspect the canonical skill references.

```text
You are using the Universal AI Execution Skill.

Task:
[TASK]

Repository context:
[REPO_CONTEXT]

Constraints:
[CONSTRAINTS]

Expected output:
[EXPECTED_OUTPUT]

Use the canonical skill router at:
skills/universal-ai-execution/SKILL.md

Use these canonical references when available:
- skills/universal-ai-execution/references/workflow-registry.yaml
- skills/universal-ai-execution/references/task-classification-rules.md
- skills/universal-ai-execution/references/output-contracts.md
- skills/universal-ai-execution/references/validation-matrix.md
- skills/universal-ai-execution/references/pr-breakdown-rules.md
- skills/universal-ai-execution/references/anti-patterns.md
- skills/universal-ai-execution/references/security-review-rules.md
- skills/universal-ai-execution/references/documentation-review-rules.md
- skills/universal-ai-execution/references/product-business-review-rules.md

Instructions:
1. Read the provided skill and reference context before deciding what to do.
2. Classify the task.
3. Select the workflow from the workflow registry. If the registry is not
   included in context, say that workflow selection is based on incomplete
   context.
4. Apply the matching output contract.
5. Inventory relevant source files or documentation before proposing changes.
6. Keep the plan and any suggested changes small, scoped, and reviewable.
7. Do not duplicate the workflow registry in your answer.
8. Do not invent unavailable repository facts.
9. Validate before claiming completion, or state exactly what could not be
   validated.
10. Report remaining risks and assumptions separately from evidence.
```

This prompt is a compatibility bridge only. It cannot make an LLM read files or
run commands unless the surrounding environment provides that capability.
