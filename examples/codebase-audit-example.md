# Codebase Audit Example

## User Request

"Review this repository end to end and tell me the biggest product, architecture, testing, and operations gaps before we plan the next quarter."

## Detected Task Type

Broad repository audit across functionality, architecture, quality, and operations.

## Selected Workflow

`full-codebase-audit`

## Why This Workflow Was Selected

The request asks for a whole-repository review across multiple concern areas, not a scoped code change or PR review.

## Expected Output Structure

- Task intake card with scope, source of truth, assumptions, and risks.
- Repository inventory.
- Business capability map.
- Functional audit and non-functional audit.
- Gap report with evidence.
- Prioritized execution roadmap.
- Validation notes and uninspected areas.

## Good Prompt

"Audit this repo for product capability coverage, architecture risks, test gaps, and operational readiness. Inventory the repo first, cite files for each finding, and end with a prioritized execution roadmap. Do not implement fixes."

## Bad Prompt To Avoid

"Make this repo production ready and clean up anything that looks bad."
