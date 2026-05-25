# Contributing

Thanks for helping improve the Universal AI Execution Skill.

This project is built through small, issue-driven changes. The goal is to keep the skill portable, predictable, and easy to review.

## Contribution Principles

- Work from an open issue when possible.
- Stay inside the current issue scope.
- Keep changes small, focused, and reviewable.
- Do not include future issue work in the current change.
- Avoid large rewrites unless an issue explicitly calls for one.
- Preserve the router, registry, reference, adapter, example, and test boundaries.
- Validate your change before marking it complete.

## Local Setup

Install lightweight development requirements:

```sh
python -m pip install -r requirements-dev.txt
```

Use `python3` instead of `python` if your environment does not provide a `python` command.

## Validation

Run:

```sh
python -m pytest
python scripts/validate-skill-structure.py
```

For registry documentation changes, also run:

```sh
uv run scripts/generate-technique-registry.py
```

## Pull Requests

Pull requests should explain:

- What changed.
- Why the change was made.
- How it was validated.
- What is intentionally left for future issues.

Keep PRs focused on one review purpose. Do not mix workflow changes, adapter changes, examples, tests, and documentation cleanup unless the issue explicitly asks for that combination.

## Templates and Skill-Local Scripts

`skills/universal-ai-execution/templates/` and `skills/universal-ai-execution/scripts/` are reserved for future issue-driven additions.

- Templates should be concise Markdown artifacts that reference canonical files without becoming hidden workflows.
- Skill-local scripts should be narrow helpers for this skill directory only.
- Migration helpers must document before/after expectations, validation, and rollback or manual recovery notes.
- Consistency checks should report drift instead of silently rewriting canonical files.
- New scripts need tests or clear validation notes.

## Workflow Registry Changes

Workflow Registry v1 is the source of truth for workflow IDs and workflow content. Registry changes should be handled carefully:

- Do not rename workflow IDs casually.
- Do not duplicate registry content into adapters, examples, or README prose.
- Regenerate `technique-registry.md` from the YAML registry when registry content changes.
- Update tests and fixtures only when an issue explicitly changes the required workflow set.

## License

By contributing, you agree that your contributions are licensed under the Apache License, Version 2.0.
