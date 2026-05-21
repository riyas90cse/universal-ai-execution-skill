# Documentation Cleanup Example

## User Request

"Our README, WORKFLOW.md, and generated registry docs disagree about what is the source of truth. Reconcile the docs without changing product behavior."

## Detected Task Type

Documentation source-of-truth cleanup.

## Selected Workflow

`documentation-source-of-truth-cleanup`

## Why This Workflow Was Selected

The request is about conflicting docs and deciding which files are authoritative.

## Expected Output Structure

- Task intake card with docs in scope and excluded docs.
- Documentation inventory.
- Code or repository reality check.
- Conflict inventory.
- Source-of-truth decision.
- Cleanup plan.
- Cleanup execution summary.
- Validation notes for links, generated docs, and source checks.

## Good Prompt

"Compare README, WORKFLOW.md, and generated registry docs against current repo state. Identify conflicting source-of-truth claims, update only the docs needed, and avoid duplicating canonical registry content."

## Bad Prompt To Avoid

"Rewrite all documentation so it sounds more polished."
