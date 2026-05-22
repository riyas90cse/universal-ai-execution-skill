# Versioning Policy

This project follows semantic versioning for public releases.

## Semantic Versioning

Version format:

`MAJOR.MINOR.PATCH`

- `MAJOR`: incompatible changes to public behavior, workflow IDs, registry format, or adapter expectations.
- `MINOR`: backward-compatible workflows, references, adapters, examples, tests, or documentation additions.
- `PATCH`: backward-compatible fixes, clarifications, generated doc updates, and test corrections.

## Workflow ID Stability

Workflow IDs are public identifiers. Once a stable release exists, workflow IDs should remain stable.

Changing or removing a workflow ID is a breaking change unless the workflow has already been deprecated and the release notes clearly explain the migration path.

## Breaking Changes

Breaking changes include:

- Renaming or removing workflow IDs.
- Changing registry structure in a way existing tools cannot read.
- Changing router expectations in a way adapters cannot follow.
- Removing output contract names or required structure without a replacement.
- Changing adapter file names or documented locations without compatibility notes.

## Deprecated Workflows

Deprecated workflows should remain in the registry for at least one minor release when possible.

Deprecation notes should include:

- Workflow ID.
- Reason for deprecation.
- Recommended replacement.
- Earliest removal version, if known.

## Registry Versioning

Workflow Registry v1 is the current registry format.

Registry format changes should update the registry `version` field and include migration notes in the changelog.

Workflow content changes that do not alter the registry format can remain within the same registry version.

## Adapter Versioning

Adapters are compatibility instructions, not native integrations.

Adapter changes should be versioned with the repository. If an adapter changes expected file location, setup instructions, or compatibility assumptions, the changelog should call that out.

Adapters must continue to point back to `skills/universal-ai-execution/SKILL.md` and Workflow Registry v1 instead of duplicating workflow definitions.
