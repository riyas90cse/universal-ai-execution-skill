# Skill-Local Scripts

This directory is reserved for helper scripts that operate specifically within `skills/universal-ai-execution/`.

No skill-local scripts are currently included.

## Purpose

Skill-local scripts should automate narrow maintenance tasks for the Universal AI Execution Skill package without changing architecture or hiding execution behavior.

This directory is separate from root-level repository scripts such as:

- `../../../scripts/generate-technique-registry.py`
- `../../../scripts/validate-skill-structure.py`

Root-level scripts validate or generate repository-wide artifacts. Skill-local scripts should be added only when the helper is specific to this skill directory.

## What Belongs Here

Future issue-driven additions may include:

- Skill-local validation helpers.
- Consistency checks for references, adapters, examples, templates, or generated docs.
- Migration helper scripts for registry, reference, or documentation transitions.
- Small wrappers that operate only under `skills/universal-ai-execution/`.

## What Does Not Belong Here

Do not place these in this directory:

- Workflow definitions.
- Router logic.
- Runtime integrations.
- CLI products.
- Heavy dependency tooling.
- Scripts that silently rewrite registry content.
- Repository-wide checks that belong in root-level `scripts/`.
- Future functionality without an approved issue.

## Source-of-Truth Boundaries

- Router: `../SKILL.md`
- Workflow definitions: `../references/workflow-registry.yaml`
- Generated readable registry: `../references/technique-registry.md`
- Output structures: `../references/output-contracts.md`
- Structure tests: `../../../tests/`
- Repository validation script: `../../../scripts/validate-skill-structure.py`

Scripts must read from canonical files and report mismatches. They must not duplicate canonical content.

## Naming Conventions

Use lowercase kebab-case Python filenames.

Examples:

- `check-reference-consistency.py`
- `validate-output-contracts.py`
- `migrate-reference-format.py`

Avoid vague names such as `helper.py`, `script.py`, or `misc.py`.

## Migration Script Guidance

Migration helper scripts must:

- Be issue-driven.
- Prefer dry-run behavior when possible.
- Print the files they would change.
- Document before/after expectations.
- Require explicit write behavior for destructive changes.
- Preserve workflow ID stability unless an approved breaking-change issue says otherwise.
- Document rollback or manual recovery steps.
- Avoid silently rewriting `workflow-registry.yaml`.

## Consistency Check Guidance

Future consistency checks may verify:

- `SKILL.md` remains router-only.
- Workflow Registry v1 IDs match test fixtures.
- `technique-registry.md` matches `workflow-registry.yaml`.
- Adapters point to canonical skill files.
- Examples use only real workflow IDs.
- README and docs use the current workflow count.
- Reference files do not duplicate registry content.
- Template files link to source-of-truth references.

## Contribution Rules

- Add a script only when an issue requires it.
- Prefer the Python standard library unless an existing dependency is already justified.
- Include tests or validation notes for new scripts.
- Keep scripts narrow, deterministic, and reviewable.
- Do not add broad runtime systems or hidden behavior.

## Current Status

This directory currently documents script boundaries only. Existing repository-level helpers live in `../../../scripts/`.
