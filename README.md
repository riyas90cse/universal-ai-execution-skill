# universal-ai-execution-skill

`universal-ai-execution-skill` is an open-source project for a portable Agent Skill and workflow registry.

It exists to help AI agents handle software work with a consistent execution discipline: classify the work, choose the right workflow, inspect the repository first, plan in small steps, make reviewable changes, and validate before claiming completion.

The project is intended for AI coding agents, agent platform builders, maintainers, and developers who want agent behavior to be safer, more predictable, and easier to review across repositories.

## Registry v1

The first version includes:

- A portable Agent Skill
- A YAML workflow registry
- 46 workflows for common agent execution scenarios
- Deterministic task classification rules
- Structured output contracts
- Generated readable registry documentation

`skills/universal-ai-execution/references/workflow-registry.yaml` is the source of truth for workflow selection.
`skills/universal-ai-execution/references/task-classification-rules.md` defines deterministic routing logic.
`skills/universal-ai-execution/references/output-contracts.md` defines structured output formats.
`skills/universal-ai-execution/references/technique-registry.md` is generated readable documentation.
`skills/universal-ai-execution/SKILL.md` remains only the router.

Regenerate the readable registry with:

```sh
uv run scripts/generate-technique-registry.py
```

Python script dependencies are declared with `uv` inline script metadata.

Adapters, examples, tests, and implementation logic will be added in future issues.

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
