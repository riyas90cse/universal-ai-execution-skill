# Refactor Plan Example

## User Request

"The billing service is hard to maintain. Create a refactor plan that preserves current behavior and can be shipped in small PRs."

## Detected Task Type

Behavior-preserving code structure improvement.

## Selected Workflow

`refactoring`

## Why This Workflow Was Selected

The request asks to improve structure while preserving behavior and limiting migration risk.

## Expected Output Structure

- Task intake card with refactor scope and non-goals.
- Current behavior that must be preserved.
- Code inventory and pain point map.
- Refactor boundary and stop conditions.
- Proposed structure.
- Migration plan with small PR execution plan.
- Before-and-after validation approach.

## Good Prompt

"Inventory the billing service, identify behavior that must not change, and propose a small-PR refactor plan with validation before and after each step. Do not add new billing features."

## Bad Prompt To Avoid

"Rewrite billing with a cleaner architecture and fix any bugs you notice."
