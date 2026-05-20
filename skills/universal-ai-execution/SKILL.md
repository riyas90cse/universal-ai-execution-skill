---
name: universal-ai-execution
description: Selects and applies the correct workflow for product, engineering, codebase, architecture, testing, security, compliance, documentation, delivery, business, GTM, hiring, interview, and career tasks.
---

# Universal AI Execution Skill

Use this skill when an agent needs to route work to the correct execution workflow before analyzing, planning, implementing, reviewing, orchestrating, or validating a task.

This `SKILL.md` is only the router. It does not contain the full workflow registry, output contracts, workflow definitions, adapters, or examples.

## Routing Flow

1. Understand the task.
2. Classify the task.
3. Select the workflow from `references/workflow-registry.yaml`.
4. Apply the output contract from `references/output-contracts.md`.
5. Enforce validation before completion.

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

## Separation of Concerns

- Router: this file selects the mode, workflow, contract, and validation path.
- Registry: `references/workflow-registry.yaml` defines detailed workflows.
- Readable registry: `references/technique-registry.md` is generated from the YAML registry.
- Contracts: `references/output-contracts.md` will define expected outputs.
