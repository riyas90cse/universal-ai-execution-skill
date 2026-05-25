# Focused Code Review Example

## User Request

"Review this pull request and tell me what should block merge."

## Routing

- Primary workflow: `code-review`
- Execution mode: `REVIEW`
- Optional focused skill: `skills/engineering/review-changes/SKILL.md`
- Output contract: Code Review

## Expected Behavior

The router selects the workflow and output contract first. The focused skill then sharpens the review around changed files, behavioral risk, findings, questions, test gaps, and verdict.

The review should lead with actionable findings. It should not expand into unrelated refactors, broad repository cleanup, or implementation unless the user explicitly asks for fixes.

## Good Prompt

"Review the diff against the issue requirements. Prioritize correctness bugs, regressions, security risks, and missing tests."

## Bad Prompt

"Review this and improve anything you notice."
