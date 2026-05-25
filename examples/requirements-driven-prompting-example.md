# Requirements-Driven Prompting Example

Use this example when the user has requirements but does not know which workflow should handle the task. The prompt should give the router enough context to classify the work, choose an execution mode, apply the right output contract, and validate the result.

## Prompt Template

```text
Use the Universal AI Execution Skill for this task.

Task:
[Describe the work in one or two sentences.]

Requirements:
- [Required outcome or acceptance criterion.]
- [Required behavior, decision, artifact, or constraint.]
- [Required validation, review, or evidence.]

Source of truth:
- [Issue, spec, files, diff, logs, policy, customer notes, or design.]

Scope:
- Include: [What is in scope.]
- Exclude: [What must not be changed or decided.]

Workflow guidance:
- If I name a valid workflow ID, use it.
- If I do not name one, classify the task and select the most specific workflow.
- If a focused skill is mapped to the selected workflow, use it as an optional accelerator.

Expected mode:
[ANALYZE_ONLY, PLAN_ONLY, IMPLEMENT, REVIEW, ORCHESTRATE, VALIDATE, or "choose based on the task."]

Expected output:
- Start with the selected workflow and execution mode.
- Follow the matching output contract.
- Separate evidence, assumptions, risks, and unknowns.
- Validate before claiming completion, or say exactly what could not be validated.
```

## Implementation Prompt

```text
Use the Universal AI Execution Skill.

Task:
Implement the requirements in the current issue.

Requirements:
- Preserve existing behavior outside the issue scope.
- Keep the change small and reviewable.
- Update only files needed for the accepted behavior.
- Run the most relevant validation available in this repository.

Source of truth:
- Current issue text.
- Existing code and tests.
- Repository instructions.

Scope:
- Include: implementation, focused tests or validation, and a concise completion summary.
- Exclude: unrelated refactors, new architecture, broad docs cleanup, and speculative features.

Workflow guidance:
- Classify the task first.
- Use the selected workflow from the registry.
- Use a mapped focused skill only if it helps execute the selected workflow.

Expected mode:
IMPLEMENT
```

## Review Prompt

```text
Use the Universal AI Execution Skill.

Task:
Review the proposed changes against the requirements.

Requirements:
- Prioritize bugs, regressions, security risks, data risks, and missing validation.
- Cite files, diffs, behavior, or tests as evidence.
- Keep style comments secondary unless they affect correctness or maintainability.

Source of truth:
- The diff or pull request.
- The issue requirements.
- Existing tests and contracts.

Scope:
- Include: findings, questions, test gaps, and verdict.
- Exclude: implementing fixes unless I explicitly ask.

Workflow guidance:
- Select the review workflow that best matches the artifact.
- Use a mapped focused skill if one exists for the selected review workflow.

Expected mode:
REVIEW
```

## Planning Prompt

```text
Use the Universal AI Execution Skill.

Task:
Turn these requirements into a reviewable implementation plan.

Requirements:
- Identify the workflow, output contract, and scope boundaries.
- Break the work into ordered steps.
- Call out dependencies, risks, and validation.
- Avoid implementation in this response.

Source of truth:
- Product or engineering requirements.
- Relevant repository files, docs, or interfaces.

Scope:
- Include: plan, risk review, and validation plan.
- Exclude: code edits and unrelated follow-up work.

Workflow guidance:
- Classify the task first.
- Use secondary workflows only as lenses, not scope expansion.

Expected mode:
PLAN_ONLY
```

## Validation Prompt

```text
Use the Universal AI Execution Skill.

Task:
Validate whether the completed work satisfies the requirements.

Requirements:
- Compare the result against each acceptance criterion.
- Run or inspect the relevant validation evidence.
- Identify failures, gaps, and remaining uncertainty.
- Do not claim completion unless validation supports it.

Source of truth:
- Requirements or issue acceptance criteria.
- Changed files, tests, generated artifacts, CI, or manual checks.

Scope:
- Include: checks performed, results, failures, and residual risk.
- Exclude: new implementation unless I ask for fixes.

Workflow guidance:
- Select the workflow that matches the completed artifact.
- Apply the validation expectations from the selected output contract.

Expected mode:
VALIDATE
```

## Bad Prompt

```text
Make this better and do whatever workflow seems useful.
```

This is weak because it hides the requirements, source of truth, scope boundaries, execution mode, and validation expectations.
