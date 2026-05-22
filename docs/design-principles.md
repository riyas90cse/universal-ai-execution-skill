# Design Principles

The Universal AI Execution Skill is designed to make AI-assisted work more predictable, reviewable, and portable without pretending to replace judgment.

## Router Over Mega-Prompt

`SKILL.md` is intentionally small. It routes the task to the right references instead of embedding every workflow, rule, contract, and example in one large prompt.

This keeps the system easier to inspect and reduces drift between routing logic and source-of-truth files.

## Registry as Source of Truth

Workflow Registry v1 lives in `skills/universal-ai-execution/references/workflow-registry.yaml`.

Workflow IDs, workflow names, categories, sequences, required outputs, validation rules, and common mistakes belong in the registry. Other files should point to the registry rather than copying it.

## Inventory Before Implementation

Agents must inspect relevant files, docs, tests, configs, and current behavior before planning or editing code.

Documentation describes intended direction only after it has been checked against code or repository state.

## Small PRs

Changes should have one review purpose. Avoid mixing unrelated refactors, behavior changes, generated file churn, adapter changes, examples, tests, and documentation cleanup.

Small PRs make review, rollback, and validation easier.

## Validation Before Completion

Agents should not claim completion until relevant checks have been run or skipped checks have been disclosed.

Validation should match the risk and scope of the change.

## Tool Portability Without Overpromising

Adapters translate usage format for different AI environments. They do not create native runtime support, guarantee compatibility, or replace the canonical skill files.

Each adapter should be realistic about what the target environment can and cannot do.

## Code as Source of Truth

For current behavior, code, tests, configuration, and generated sources are stronger evidence than prose.

When docs and code disagree, mark the docs stale unless the issue explicitly asks for intended future behavior.

## Docs as Intended Direction After Validation

Documentation should be concise, linked, and grounded in current repository state.

Docs can describe direction, but they should not imply future work is already implemented.
