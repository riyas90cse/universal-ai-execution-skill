# universal-ai-execution-skill

`universal-ai-execution-skill` is an open-source project for a portable Agent Skill and workflow registry.

It exists to help AI agents handle software work with a consistent execution discipline: classify the work, choose the right workflow, inspect the repository first, plan in small steps, make reviewable changes, and validate before claiming completion.

The project is intended for AI coding agents, agent platform builders, maintainers, and developers who want agent behavior to be safer, more predictable, and easier to review across repositories.

## Planned Scope

The first version will contain:

- A portable Agent Skill
- A workflow registry
- 46 workflows for common agent execution scenarios

The current repository includes the initial skill router at `skills/universal-ai-execution/SKILL.md`. The full workflow registry, workflows, adapters, examples, tests, and implementation logic will be added in future issues.

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
