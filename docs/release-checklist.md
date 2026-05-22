# Release Checklist

Use this checklist before tagging a release.

## Required Checks

- [ ] Tests pass with `python -m pytest`.
- [ ] Structure validation passes with `python scripts/validate-skill-structure.py`.
- [ ] All 46 workflows are verified by tests.
- [ ] README is updated.
- [ ] README links are checked.
- [ ] Examples are reviewed.
- [ ] No stale workflow-count wording remains; the expected count is 46 workflows.
- [ ] License is present.
- [ ] Security policy is present.
- [ ] Changelog is updated.
- [ ] Version tag is prepared.

Use `python3` instead of `python` if the local environment does not provide a `python` command.

## Documentation Review

- [ ] README explains what the project is, why it exists, who should use it, and how it works.
- [ ] README includes usage notes for Codex, Claude Code, generic LLMs, Cursor, GitHub Copilot, and Symphony-style orchestration.
- [ ] README links to examples, roadmap, contribution guide, security policy, changelog, and license.
- [ ] Design principles are current.
- [ ] Roadmap is current.
- [ ] Versioning policy is current.

## Release Notes

- [ ] Changelog has an entry for the release.
- [ ] Breaking changes are called out, if any.
- [ ] Deprecated workflows are called out, if any.
- [ ] Adapter compatibility limitations are clear.

## Final Review

- [ ] No unsupported native compatibility claims.
- [ ] No wording says the skill can substitute for human review.
- [ ] No wording promises correctness.
- [ ] Workflow Registry v1 remains the source of truth.
- [ ] Generated registry was regenerated if registry YAML changed.
