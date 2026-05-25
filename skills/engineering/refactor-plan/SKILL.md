---
name: refactor-plan
description: Plan behavior-preserving refactors and repository restructuring with clear boundaries, migration steps, and validation controls.
---

# Refactor Plan

## Purpose

Use this focused skill to design a behavior-preserving refactor or repository restructuring plan. It keeps the work incremental, testable, and reversible while avoiding opportunistic feature changes.

## Mapped Workflows

- `refactoring`
- `repo-restructuring`
- `legacy-migration`
- `framework-version-upgrade`

## When To Use

- The user asks to refactor while preserving behavior.
- Module boundaries, dependencies, or directory structure need cleanup.
- A migration or upgrade needs staged compatibility planning.
- The request is planning-first or risk-heavy before implementation.

## Required Inputs

- Current pain points and affected modules.
- Behavior that must not change.
- Existing tests and validation commands.
- Target shape, constraints, or migration deadline if known.

## Process

1. Inventory current behavior, ownership boundaries, imports, tests, and callers.
2. Define the refactor boundary and explicit non-goals.
3. Identify compatibility needs and stop conditions.
4. Propose the smallest sequence of behavior-preserving steps.
5. Attach validation to each step before moving to the next.
6. Call out rollback, shims, or temporary duplication when useful for safety.

## Output Contract

Return a refactor plan with:

- Current behavior to preserve.
- Pain points with evidence.
- Refactor boundary and exclusions.
- Proposed target shape.
- Incremental migration steps.
- Risk controls.
- Validation plan.

## Validation Checklist

- The plan states what behavior must remain unchanged.
- Each step is small enough to review independently.
- Validation proves before-and-after behavior where possible.
- Feature work is excluded unless explicitly requested.
- Rollback or stop conditions are clear for risky steps.

## Common Mistakes

- Renaming or moving files before understanding callers.
- Combining refactor, feature work, and cleanup in one change.
- Treating tests as optional for behavior-preserving work.
- Designing a final architecture without an incremental path.
