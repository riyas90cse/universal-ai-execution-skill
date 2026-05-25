---
name: universal-ai-execution
description: Selects and applies the correct workflow for product, engineering, codebase, architecture, testing, security, compliance, documentation, delivery, business, GTM, hiring, interview, and career tasks.
---

# Universal AI Execution Skill

Use this skill when an agent needs to route work to the correct execution workflow before analyzing, planning, implementing, reviewing, orchestrating, or validating a task.

This `SKILL.md` is only the router. It does not contain the full workflow registry, classification rules, output contracts, workflow definitions, adapters, or examples.

## Routing Flow

1. Understand the task.
2. Classify the task using `references/task-classification-rules.md`.
3. Select the workflow from `references/workflow-registry.yaml`.
4. Check whether the selected workflow has an optional focused skill mapping.
5. Apply the output contract from `references/output-contracts.md`.
6. Enforce validation before completion.

## Focused Skill Accelerators

Focused skills are optional deeper playbooks for selected workflows. The router must still work when no focused skill exists or when a focused skill is unavailable.

Use focused skills this way:

1. Route through this skill first.
2. Treat the registry workflow and output contract as authoritative.
3. Load a mapped focused skill only as an accelerator for execution detail.
4. Do not use focused skills to rename workflow IDs, add registry content, or bypass validation.

## Execution Modes

- `ANALYZE_ONLY`: inspect, explain, and report without planning or changing files.
- `PLAN_ONLY`: produce a bounded plan without implementing changes.
- `IMPLEMENT`: make the smallest scoped change that satisfies the task.
- `REVIEW`: evaluate existing work for correctness, risks, and gaps.
- `ORCHESTRATE`: coordinate multi-step or multi-agent work while preserving scope.
- `VALIDATE`: verify completed work against requirements before claiming done.

## Non-Negotiable Rules

- Inventory before codebase implementation.
- Code is source of truth for current behavior.
- Docs are intended direction only after validation against code.
- Small PRs only.
- No giant rewrites.
- Preserve existing architecture and conventions.
- Security-sensitive work requires abuse-case review.
- Database work requires migration and rollback thinking.
- UI/backend work requires contract mapping.

## Guardrail References

- Validation: `references/validation-matrix.md`
- PR breakdown: `references/pr-breakdown-rules.md`
- Anti-patterns: `references/anti-patterns.md`
- Security review: `references/security-review-rules.md`
- Documentation review: `references/documentation-review-rules.md`
- Product and business review: `references/product-business-review-rules.md`

## Separation of Concerns

- Router: this file selects the mode, workflow, contract, and validation path.
- Classification rules: `references/task-classification-rules.md` defines deterministic routing logic.
- Registry: `references/workflow-registry.yaml` defines detailed workflows.
- Focused skill mappings: `references/workflow-registry.yaml` maps selected workflows to optional focused skill paths.
- Readable registry: `references/technique-registry.md` is generated from the YAML registry.
- Contracts: `references/output-contracts.md` defines expected output structures.
