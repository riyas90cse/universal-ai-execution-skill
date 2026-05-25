# Workflow Policy

Work in this repository is issue-driven and release-oriented.

## Execution Rules

- Read the issue and repository instructions before editing.
- Use `skills/universal-ai-execution/SKILL.md` as the canonical router.
- Keep changes small and reviewable.
- Do not perform giant rewrites.
- Do not change workflows, router behavior, adapters, examples, tests, or docs unless the current issue asks for that concern.
- Validate before claiming completion.

## Review Boundaries

- Router changes belong in `skills/universal-ai-execution/SKILL.md`.
- Workflow content belongs in `skills/universal-ai-execution/references/workflow-registry.yaml`.
- Generated readable registry content belongs in `technique-registry.md` and should be regenerated, not manually edited.
- Guardrail rules belong in focused reference files.
- Adapter files should translate usage format only.
- Examples should demonstrate real workflow IDs only.
- Tests should validate structure and registry integrity, not simulate AI behavior.
- Templates should provide reusable output shapes without redefining workflows.
- Skill-local scripts should be narrow migration or consistency helpers and should not replace root-level validation.

## Release Readiness

Before a release candidate:

- Run `python -m pytest`.
- Run `python scripts/validate-skill-structure.py`.
- Regenerate the technique registry if the YAML registry changed.
- Check README links and naming consistency.
- Confirm the release checklist in `docs/release-checklist.md`.
- Confirm `CHANGELOG.md`, `SECURITY.md`, `LICENSE`, and versioning docs are current.

Use `python3` instead of `python` if your environment does not provide a `python` command.
