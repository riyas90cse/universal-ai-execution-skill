# universal-ai-execution-skill

`universal-ai-execution-skill` is an open-source project for a portable Agent Skill and workflow registry.

It exists to help AI agents handle software work with a consistent execution discipline: classify the work, choose the right workflow, inspect the repository first, plan in small steps, make reviewable changes, and validate before claiming completion.

The project is intended for AI coding agents, agent platform builders, maintainers, and developers who want agent behavior to be safer, more predictable, and easier to review across repositories.

## Adapters

Adapters translate the Universal AI Execution Skill into instruction formats for
different AI environments. They do not replace `skills/universal-ai-execution/SKILL.md`
or duplicate the workflow registry.

- Codex: copy or merge `adapters/codex/AGENTS.md` into a repository `AGENTS.md`
  file so Codex is directed to the canonical skill router and registry.
- Generic LLM: paste `adapters/generic-llm/universal-invocation-prompt.md` into
  an LLM session and fill in `[TASK]`, `[REPO_CONTEXT]`, `[CONSTRAINTS]`, and
  `[EXPECTED_OUTPUT]`. Include relevant skill files in context when the LLM
  cannot read the repository.
- Cursor: place `adapters/cursor/universal-ai-execution.mdc` in a Cursor rules
  location, such as `.cursor/rules/`, when that environment supports `.mdc`
  rules.
- GitHub Copilot: use `adapters/github-copilot/copilot-instructions.md` as
  repository or chat instruction text where Copilot custom instructions are
  supported.
- Symphony-style workflow: use `adapters/symphony/WORKFLOW.md` as issue-driven
  orchestration guidance. It is not a runtime implementation.

## Examples

Examples show realistic workflow selection, expected output structure, and good
versus bad prompting behavior.

- [Codebase audit](examples/codebase-audit-example.md)
- [Backend/UI integration audit](examples/backend-ui-integration-example.md)
- [Security audit](examples/security-audit-example.md)
- [MVP planning](examples/mvp-planning-example.md)
- [Refactor plan](examples/refactor-plan-example.md)
- [Documentation cleanup](examples/documentation-cleanup-example.md)
- [RBAC design](examples/rbac-design-example.md)
- [Testing strategy](examples/test-strategy-example.md)
- [GTM strategy](examples/gtm-strategy-example.md)
- [Career positioning](examples/career-positioning-example.md)

## Registry v1

The first version includes:

- A portable Agent Skill
- A YAML workflow registry
- 46 workflows for common agent execution scenarios
- Deterministic task classification rules
- Structured output contracts
- Guardrail references for validation, PR breakdown, security, docs, product/business review, and anti-patterns
- Lightweight adapters for Codex, generic LLMs, Cursor, GitHub Copilot, and Symphony-style orchestration
- Practical examples for common workflow selections
- Generated readable registry documentation

`skills/universal-ai-execution/references/workflow-registry.yaml` is the source of truth for workflow selection.
`skills/universal-ai-execution/references/task-classification-rules.md` defines deterministic routing logic.
`skills/universal-ai-execution/references/output-contracts.md` defines structured output formats.
`skills/universal-ai-execution/references/validation-matrix.md` and related guardrail references define safety checks for execution discipline.
`skills/universal-ai-execution/references/technique-registry.md` is generated readable documentation.
`skills/universal-ai-execution/SKILL.md` remains only the router.

Regenerate the readable registry with:

```sh
uv run scripts/generate-technique-registry.py
```

Python script dependencies are declared with `uv` inline script metadata.

## Local Validation

Install lightweight development requirements, then run the structure tests and
standalone validation script:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest
python scripts/validate-skill-structure.py
```

Use `python3` instead of `python` if your environment does not provide a
`python` command.

The tests validate package structure, router/registry separation, required
reference files, adapter files, and all 46 workflow IDs in both registry outputs.

Implementation logic will be added in future issues.

## Core Principle

- Classify the work
- Select the workflow
- Inventory first
- Plan small
- Execute safely
- Validate before claiming done

## Status

This repository is being built incrementally through small, issue-driven changes.

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).
