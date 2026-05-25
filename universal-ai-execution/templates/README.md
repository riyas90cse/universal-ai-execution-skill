# Templates

This directory is reserved for reusable Universal AI Execution Skill template artifacts.

No skill-local templates are currently included.

## Purpose

Templates in this directory should help agents produce consistent, reviewable outputs without redefining workflows or hiding execution logic.

Templates are human/agent-facing Markdown artifacts, not workflow definitions and not runtime behavior.

## What Belongs Here

Future issue-driven additions may include:

- Task intake templates.
- Output contract skeletons.
- Review report templates.
- Release or readiness check templates.
- Adapter snippet templates, when a future issue needs reusable adapter wording.
- Migration planning templates, when they document planning structure rather than migration logic.

## What Does Not Belong Here

Do not place these in this directory:

- Workflow definitions.
- Workflow ID lists copied from the registry.
- Router logic.
- Output contract source-of-truth content.
- Adapter runtime claims.
- Generated registry content.
- Large prompt dumps.
- Future feature scaffolding without an approved issue.

## Source-of-Truth Boundaries

- Router: `../SKILL.md`
- Workflow definitions: `../references/workflow-registry.yaml`
- Generated readable registry: `../references/technique-registry.md`
- Output structures: `../references/output-contracts.md`
- Classification rules: `../references/task-classification-rules.md`
- Guardrails: `../references/*.md`

Templates must reference these files instead of duplicating canonical content.

## Naming Conventions

Use lowercase kebab-case names ending in `-template.md`.

Examples:

- `task-intake-template.md`
- `code-review-output-template.md`
- `migration-plan-template.md`

Avoid vague names such as `template.md`, `new-template.md`, or `misc.md`.

## Migration Template Guidance

Migration templates may help structure planning for registry, documentation, adapter, or output-contract transitions.

They must:

- Be issue-driven.
- Name the current state and target state.
- Include before/after expectations.
- Include validation and rollback or manual recovery notes.
- Preserve workflow ID stability unless an approved breaking-change issue says otherwise.
- Avoid implying that migration steps were executed.

## Contribution Rules

- Add a template only when an issue requires it.
- Keep templates concise and practical.
- Do not turn templates into hidden workflows.
- Link to source-of-truth references instead of copying registry or router content.
- Document how the template should be validated.

## Current Status

This directory currently documents template boundaries only. Existing output structures live in `../references/output-contracts.md`.
