---
name: review-changes
description: Review diffs, pull requests, and planned PR slices for correctness, regressions, and missing validation.
---

# Review Changes

## Purpose

Use this focused skill to review a patch, pull request, commit, or proposed change sequence. It sharpens the code-review workflow around evidence, behavioral risk, test gaps, and reviewable change boundaries.

## Mapped Workflows

- `code-review`
- `pull-request-planning`

## When To Use

- The user asks for a review of a diff, PR, commit, or patch.
- A larger change needs to be split into reviewable PRs.
- Existing review comments need risk-focused triage.
- The task is to evaluate changes rather than implement new behavior.

## Required Inputs

- Diff, PR, commit range, branch, or file list.
- Issue requirements or intended behavior.
- Relevant tests, CI status, or validation expectations.
- Known out-of-scope areas.

## Process

1. Inventory the changed files and intended behavior before judging the patch.
2. Compare implementation against requirements, existing contracts, and local conventions.
3. Prioritize findings that can cause bugs, regressions, security issues, data loss, or failed validation.
4. Identify missing or weak tests tied to concrete risk.
5. For PR planning, split work by dependency order and review surface.
6. Keep style or preference comments secondary unless they affect maintainability or correctness.

## Output Contract

Return a review with:

- Scope reviewed.
- Findings ordered by severity with file or area evidence.
- Questions for the author.
- Test and validation gaps.
- PR sequencing advice when requested.
- Verdict or readiness recommendation.

## Validation Checklist

- Findings cite concrete evidence from the diff or repository.
- Severity reflects user impact and likelihood.
- The review does not request unrelated refactors.
- Test gaps are tied to changed behavior.
- PR splits are independently reviewable and validated.

## Common Mistakes

- Leading with summary instead of findings.
- Reporting speculative issues without evidence.
- Mixing unrelated cleanup into a review request.
- Approving based on passing tests without reading the change.
