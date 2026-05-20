# Anti-Patterns

This file defines behaviors agents must avoid. It is a guardrail layer, not a
workflow definition.

## Stop Rules

Stop and narrow scope when a task starts to include unrelated behavior, new architecture,
new tooling, or future issue work not requested by the user.

Stop and validate when a change touches security, data migration, production release,
public API contracts, or broad refactors.

## Anti-Pattern Checklist

| Anti-pattern | Why it is unsafe | Required correction |
| --- | --- | --- |
| Giant rewrite | Destroys reviewability and hides regressions | Split into small, behavior-preserving steps |
| Prompt dumping | Produces unreviewed bulk content without repo fit | Convert prompts into scoped rules or code tied to source files |
| Trusting stale docs | Repeats intended behavior instead of actual behavior | Check code, config, tests, registry, or current source of truth |
| Mock-data UI pretending to be integrated | Makes incomplete features appear production-ready | Label mock data and map missing backend contracts |
| Mixing refactor with behavior change | Makes defects hard to attribute | Separate structure changes from functional changes |
| Adding libraries without justification | Increases maintenance, security, and bundle risk | Use existing dependencies or justify need, alternatives, and impact |
| Security changes without negative tests | Can prove only the happy path | Add denied-path, abuse-case, or authorization tests |
| Database migration without rollback thinking | Can leave production data unrecoverable | Define rollback, backup, or contingency before claiming readiness |
| Deleting docs/code without inventory | Can remove live behavior or needed knowledge | Inventory references, imports, links, and owners before deletion |
| Duplicate architecture patterns | Creates competing ways to solve the same problem | Follow the existing local pattern or explain the exception |
| Claiming completion without validation | Misrepresents risk and hides failures | Run relevant checks or state exactly what was not validated |
| Solving future issues inside the current PR | Bloats scope and complicates review | Move future work to follow-up notes or separate issues |

## Overengineering Signals

- Adding abstractions before two concrete use cases exist.
- Creating adapters, plugins, or frameworks when a local helper would satisfy the issue.
- Adding configuration for options not requested.
- Replacing stable patterns because a different pattern is preferred.
- Creating generalized naming, routing, or registry systems outside current scope.
- Introducing dependencies for small transformations available in the platform or repo.

## Unsafe Refactor Signals

- Moving files before understanding imports, runtime entry points, or ownership.
- Renaming public APIs without compatibility checks.
- Changing data shape while claiming behavior preservation.
- Removing tests because they are inconvenient.
- Combining cleanup with bug fixes across many modules.
- Changing formatting across untouched files in a semantic PR.

## Completion Claims to Avoid

Do not say:

- "Done" when validation failed or was skipped without disclosure.
- "Integrated" when the UI still uses mock data.
- "Secure" when only happy-path tests were run.
- "Backward compatible" without checking existing consumers.
- "Docs updated" when docs were not checked against current code or source files.

## Review Prompts

Before final output, ask:

- Did this stay inside the current issue scope?
- Did this change only the files needed for the concern?
- Did this preserve existing architecture and naming?
- Did this avoid future features and generic infrastructure?
- Did this report validation honestly?
