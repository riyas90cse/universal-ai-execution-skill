---
name: full-codebase-audit
description: Audit a repository across architecture, behavior, tests, operations, and maintainability while keeping findings evidence-based.
---

# Full Codebase Audit

## Purpose

Use this focused skill to perform a broad repository audit without turning it into an unbounded rewrite. It emphasizes inventory, capability mapping, evidence-backed findings, and a prioritized remediation roadmap.

## Mapped Workflows

- `full-codebase-audit`
- `backend-ui-integration-audit`
- `performance-scalability-review`
- `observability-monitoring`

## When To Use

- The user asks for a full repository or codebase audit.
- Multiple system areas must be inspected together.
- The desired output is a findings report or roadmap rather than immediate edits.
- Architecture, testing, operational, and maintainability risks need a single view.

## Required Inputs

- Repository path and audit scope.
- User goals, quality bar, or target audience.
- Excluded areas or known constraints.
- Available validation commands, logs, or CI results.

## Process

1. Inventory entry points, major modules, data stores, integrations, tests, and deployment surfaces.
2. Map user-facing or system capabilities to implementation areas.
3. Inspect representative paths before making claims about broad patterns.
4. Group findings by severity and affected capability.
5. Separate confirmed issues from hypotheses and uninspected areas.
6. Produce a prioritized roadmap with validation and ownership hints.

## Output Contract

Return a codebase audit with:

- Scope and exclusions.
- Inventory of inspected areas.
- Capability map.
- Findings with severity, evidence, impact, and recommendation.
- Gaps and unknowns.
- Prioritized roadmap.
- Validation notes.

## Validation Checklist

- Claims are backed by files, commands, logs, or inspected behavior.
- Broad conclusions are based on representative evidence.
- Findings are ranked by risk and impact.
- The roadmap is incremental and reviewable.
- Uninspected areas are named rather than implied covered.

## Common Mistakes

- Auditing only filenames or docs without code evidence.
- Producing a rewrite plan instead of prioritized findings.
- Treating all issues as equally urgent.
- Hiding uncertainty to make the report sound complete.
