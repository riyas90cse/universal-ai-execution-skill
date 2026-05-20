# Documentation Review Rules

This file defines documentation integrity guardrails. It does not define
documentation workflows or registry entries.

## Core Rules

- Inventory before cleanup.
- Code, configuration, generated sources, and current registry files are stronger evidence than stale prose.
- Do not delete, merge, or rewrite docs without checking references and ownership.
- Separate current behavior from intended future direction.
- Keep repo-local docs concise and operational unless the project explicitly stores detailed guides in the repo.

## Inventory Before Cleanup

Before changing docs, identify:

- Files in scope and files intentionally out of scope.
- Audience: user, maintainer, contributor, operator, security reviewer, or agent.
- Source of truth for each material claim.
- Links, generated files, scripts, examples, and references pointing at the docs.
- Conflicting or duplicate docs that mention the same behavior.

## Code Reality Check

For behavior claims, check at least one relevant source:

- Code paths, entry points, routes, commands, or configs.
- Tests or fixtures proving behavior.
- Registry or generated files when docs describe registry content.
- Scripts that generate documentation.
- Current README, contributing, workflow, or security policy files.

If code and docs disagree, mark the docs as stale unless the issue explicitly says the docs describe intended future behavior.

## Conflict Detection

Flag conflicts when two docs disagree on:

- Setup commands, runtime requirements, or supported versions.
- Architecture, source of truth, or ownership.
- Security posture, permissions, or data handling.
- Feature status, MVP scope, roadmap, or release readiness.
- Generated file edit policy.

## Source-of-Truth Rules

- Registry facts belong in the registry source or generated registry output, not hand-copied into unrelated docs.
- Generated docs should not be edited manually.
- README should summarize stable project usage and point to deeper references.
- Security policy should own vulnerability reporting and security support expectations.
- Workflow/contribution docs should own collaboration and PR expectations.
- Reference files should own detailed rules for their specific concern.

## Delete, Merge, Rewrite Decision Matrix

| Condition | Action |
| --- | --- |
| Duplicate doc says the same current thing | Merge or link to the stronger source |
| Duplicate doc conflicts with current source | Rewrite or remove the stale claim |
| Doc describes removed behavior | Delete only after reference inventory |
| Doc describes future work | Mark as future or move out of current-behavior docs |
| Doc is too verbose but accurate | Shorten without changing meaning |
| Generated doc is stale | Regenerate from source instead of manual editing |

## Stale Documentation Handling

- Name the stale claim.
- Name the source that proves it stale.
- Replace it with current behavior or remove it.
- If current behavior is unknown, say `Unknown` instead of guessing.
- Do not preserve stale text because it sounds useful.

## Legacy and MVP References

- Keep old MVP or legacy notes only when they explain current compatibility, migration, or support behavior.
- Remove or mark legacy references that imply obsolete behavior is still current.
- Do not let roadmap language masquerade as shipped behavior.

## Repo-Local vs External Docs

- Repo-local docs should cover install, development, validation, contribution, security, architecture decisions, and source-of-truth references.
- Detailed tutorials, marketing copy, long product narratives, and external operating procedures should be linked or summarized unless the repo is the chosen source.
- Prefer links to authoritative references over copying long content into multiple files.

## Documentation Validation

Report:

- Files inventoried.
- Source files checked.
- Claims corrected or removed.
- Links or generated docs checked when relevant.
- Remaining unknowns or deferred doc candidates.
