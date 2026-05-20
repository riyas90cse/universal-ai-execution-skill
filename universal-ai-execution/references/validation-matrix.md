# Validation Matrix

This file defines practical validation guardrails. It does not define workflows,
execution logic, or registry entries.

## Validation Principles

- Match validation to the risk and scope of the change.
- Prefer the smallest check that can prove the claim.
- Run existing repo-local checks before inventing new ones.
- Treat skipped validation as a disclosed risk, not as success.
- Do not claim completion when required validation failed or was not run.
- For codebase work, include command names and results in the final output.

## Validation Matrix

| Check | Required when | Evidence to report | Stop condition |
| --- | --- | --- | --- |
| Unit tests | Business logic, helpers, services, validators, or reducers change | Test command and result | Relevant unit tests fail |
| Integration tests | Multiple modules, database access, queues, external services, or app boundaries change | Command, environment, and result | Boundary behavior is unverified |
| Contract tests | API request/response, events, schemas, SDK types, UI data contracts, or public interfaces change | Contract checked and incompatible fields listed | Producer and consumer disagree |
| E2E tests | User-facing flows, auth, checkout, onboarding, critical paths, or cross-screen behavior change | Flow name, tool, and result | Critical user path cannot be proven |
| Smoke tests | Release, deploy, startup, build, routing, or service boot behavior changes | Minimal boot or health result | App cannot start or core route fails |
| Regression tests | Bug fixes, behavior preservation, refactors, migrations, or fragile paths change | Failing-before or targeted regression evidence | Original failure is not covered |
| Security tests | Auth, authorization, RBAC, tenant isolation, secrets, uploads, input validation, public APIs, or dependency risk changes | Positive and negative security checks | Missing negative test for security-sensitive change |
| Performance checks | Hot paths, database queries, caching, pagination, startup, rendering, or concurrency change | Baseline, changed result, or bounded rationale | Performance claim lacks measurement or limit |
| Accessibility checks | Interactive UI, navigation, forms, modals, color, focus, labels, or keyboard behavior change | Tool/manual check and affected screen | Keyboard or screen-reader path is broken |
| Migration validation | Schema, data migration, backfill, indexes, file format, or storage layout changes | Forward migration check and data integrity note | Migration cannot be applied safely |
| Rollback validation | Release, migration, config, infra, or destructive change can affect production state | Rollback path or explicit non-rollback rationale | No rollback or contingency for risky change |
| Manual verification | Automated coverage is unavailable, too expensive, or cannot inspect visual/product behavior | Exact steps, expected result, actual result | Steps are vague or not reproducible |

## Definition of Done

A task is done only when all applicable items are true:

- Scope matches the current issue or request.
- Relevant source files or authoritative docs were inspected.
- Changes are minimal and reviewable.
- Required tests or checks were run, or the reason for skipping is explicit.
- Security-sensitive changes include negative or abuse-case validation.
- Database or migration changes include rollback or contingency thinking.
- Documentation claims were checked against code, registry, or current repo state.
- Final output states changed files, validation performed, and remaining risks.

## Validation Selection Rules

- For docs-only changes, validate links, filenames, generated docs, formatting, and source-of-truth references.
- For tests-only changes, validate that the new test fails for the targeted bug when feasible, then passes after the fix.
- For refactors, validate before and after behavior with the same checks.
- For API or UI contract changes, validate producer and consumer expectations together.
- For migrations, validate forward path, rollback path, and data preservation assumptions.
- For security fixes, validate both allowed and denied behavior.
- For release readiness, validate build, smoke path, rollback path, and known blocking risks.

## Reporting Rules

- Say `Passed`, `Failed`, `Skipped`, or `Not applicable` for each relevant validation class.
- Include exact commands for automated checks.
- Include exact manual steps for manual checks.
- Do not hide failed checks behind broad summaries.
- Do not convert validation gaps into future work unless the current scope makes them impossible to resolve.
