# PR Breakdown Rules

This file defines small PR discipline. It does not create workflows or execution
logic.

## Core Rules

- One PR should have one review purpose.
- Split by risk boundary before splitting by file count.
- Keep behavior changes separate from mechanical movement when possible.
- Keep refactors separate from feature work unless the refactor is required for the feature and remains local.
- Do not include future issue work to "save time."
- Every PR must be independently reviewable, testable, and reversible enough for its risk.

## When to Split

Split the work when any of these are true:

- The diff crosses unrelated domains, such as data model, backend behavior, UI, docs, and tests.
- Review requires different specialists, such as security, database, design, or infrastructure.
- A rollback would need to undo only part of the change.
- The implementation needs compatibility or sequencing.
- The PR contains both behavior change and broad cleanup.
- The PR is hard to summarize in one sentence.

## Standard PR Types

| PR type | Use for | Must include | Must not include |
| --- | --- | --- | --- |
| Foundation PR | Shared scaffolding, config, flags, types, interfaces, or no-op wiring | Clear reason and no behavior change unless explicit | Feature behavior, broad cleanup, unrelated formatting |
| Data model PR | Schema, migrations, indexes, seed shape, persistence boundaries | Migration validation and rollback thinking | UI polish, unrelated API behavior |
| Backend PR | Server behavior, services, jobs, authorization, integrations | Unit/integration validation and risk notes | UI-only changes, docs rewrites |
| API contract PR | Request/response schema, events, public types, SDK shape | Producer/consumer contract mapping | Internal refactors unrelated to the contract |
| UI PR | Screens, components, state, accessibility, visual behavior | Manual or automated UI verification | Backend contract redesign unless scoped |
| Test PR | Test coverage, fixtures, harnesses, regression tests | What risk or behavior the tests prove | Product behavior changes |
| Docs PR | README, references, runbooks, architecture notes | Source-of-truth check | Code behavior changes unless docs generation requires it |
| Cleanup PR | Dead code removal, formatting, local simplification | Inventory proving removal is safe | Functional changes, architecture rewrites |

## Recommended Sequence

Use this order only when those concerns exist:

1. Foundation PR for non-behavioral preparation.
2. Data model PR for schema or storage changes.
3. API contract PR for public or cross-boundary interfaces.
4. Backend PR for behavior behind the contract.
5. UI PR for user-facing behavior.
6. Test PR when tests can land independently.
7. Docs PR for user, maintainer, or operator guidance.
8. Cleanup PR after behavior is proven.

Do not create empty PR types to follow the sequence.

## What Not to Mix

- Refactor plus new behavior.
- Migration plus UI redesign.
- Security fix plus unrelated dependency upgrades.
- API contract change plus broad backend cleanup.
- Test harness rewrite plus feature implementation.
- Documentation rewrite plus code removal.
- Generated file churn plus manual logic changes.
- Formatting-only changes plus semantic changes.
- Future roadmap work plus current issue work.

## PR Sizing Checks

Before opening or describing a PR, confirm:

- The title can name the single purpose.
- The summary can list all behavior changes in three bullets or fewer.
- The validation is specific to the changed surface.
- The rollback or mitigation story is understandable.
- The reviewer can review without reconstructing unrelated context.

## Exceptions

Combining concerns is allowed only when separation would make the system fail or leave an invalid intermediate state.
When combining concerns, state the coupling and keep the combined surface as small as possible.
