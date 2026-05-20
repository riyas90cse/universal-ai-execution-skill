# Task Classification Rules

This file defines deterministic routing logic for the Universal AI Execution Skill.
It does not define workflow steps, workflow outputs, or validation rules.

Source of truth:

- Workflow definitions: `workflow-registry.yaml`
- Output formats: `output-contracts.md`
- Router entrypoint: `../SKILL.md`

## Classification Result

Every routed task must produce these fields before workflow execution:

- `task_type`: short normalized task description.
- `primary_workflow`: one workflow id from `workflow-registry.yaml`, or `default_workflow_sequence` when no exact workflow matches.
- `secondary_workflows`: zero or more workflow ids used only as review lenses or follow-up candidates.
- `execution_mode`: one of `ANALYZE_ONLY`, `PLAN_ONLY`, `IMPLEMENT`, `REVIEW`, `ORCHESTRATE`, or `VALIDATE`.
- `output_contract`: one contract name from `output-contracts.md`.
- `scope`: explicit included and excluded work.
- `source_of_truth`: files, code, issue, diff, product brief, policy, or user-provided material used for routing.
- `ambiguity_status`: `none`, `resolved_by_rule`, or `needs_clarification`.
- `routing_reason`: one sentence naming the decisive signal.

## Decision Order

Apply these rules in order. Once a primary workflow is selected, continue only to choose secondary workflows, execution mode, and output contract.

1. Honor an explicit workflow id named by the user if it exists in `workflow-registry.yaml`.
2. Honor an explicit execution mode when the user asks for one by name.
3. Identify safety, compliance, production, data, authorization, or tenant-isolation signals and apply the escalation rules below.
4. Route by artifact type when the user names a diff, pull request, repository, issue, incident, API, database, UI, release, or document set.
5. Route by action verb when the artifact is generic: implement, review, audit, refactor, migrate, upgrade, plan, validate, or explain.
6. Route by domain intent for product, business, career, hiring, GTM, pricing, marketplace, AI, or analytics work.
7. If no rule matches, compare the user intent against `when_to_use` entries in `workflow-registry.yaml` and choose the most specific single match.
8. If still unmatched, use the registry default workflow sequence and the nearest output contract.

## Execution Mode Rules

Use only the execution modes defined in `../SKILL.md`.

| User signal | Execution mode |
| --- | --- |
| "explain", "inspect", "summarize", "analyze", "compare", "what is" | `ANALYZE_ONLY` |
| "plan", "design", "scope", "propose", "outline", "break down" | `PLAN_ONLY` |
| "implement", "fix", "add", "update", "create", "remove", "refactor", "migrate", "upgrade" | `IMPLEMENT` |
| "review", "audit", "assess", "critique", "find risks", "evaluate" | `REVIEW` |
| "coordinate", "orchestrate", "delegate", "split across agents", "sequence work" | `ORCHESTRATE` |
| "validate", "verify", "test", "check completion", "confirm readiness" | `VALIDATE` |

Tie breakers:

- If the user says "only", "do not change files", or "no implementation", do not select `IMPLEMENT`.
- If implementation and validation are both requested, select `IMPLEMENT` and include validation in the contract.
- If review/audit and fix are both requested but no specific finding is provided, select `REVIEW` first and list fixes as recommendations.
- If a user asks to plan and then implement in the same task, select `IMPLEMENT`; the plan is a required execution step, not a separate mode.
- If the task is explicitly about checking completed work, select `VALIDATE` even when the workflow domain is engineering, product, or release.

## Primary and Secondary Workflow Rules

- The primary workflow controls the main output and validation path.
- Secondary workflows are lenses only. They must not expand scope unless the user explicitly asks for that additional work.
- Use a secondary workflow when a task has a dominant action plus a material cross-cutting concern, such as security, compliance, database migration, API contract risk, or UI/backend contract risk.
- When two workflow ids are explicitly named, the first named workflow is primary unless the user provides a different order.
- When one action verb applies to multiple domains, choose the workflow for the action as primary and add the domain workflow as secondary.
- When multiple unrelated actions are requested, select `ORCHESTRATE` only if the user asks for coordination; otherwise choose the highest-priority actionable item and mark the rest out of scope.
- Action priority for unrelated actions is safety review, validation of completed work, implementation, review/audit, planning/design, then analysis/explanation.

## Keyword and Intent Mapping

This table covers common routing triggers only. It is not a copy of the workflow registry.

| User intent or signal | Primary workflow |
| --- | --- |
| Validate a startup idea, assess a new product bet, test customer demand | `product-startup-idea` |
| Plan MVP scope, cut features, define first useful version | `mvp-planning` |
| Design or review system architecture, platform direction, major technical design | `technical-architecture` |
| Implement scoped code, fix a bug, add a small feature | `coding-implementation` |
| Audit a full repository or broad codebase quality | `full-codebase-audit` |
| Clean conflicting docs, identify authoritative docs, reconcile source of truth | `documentation-source-of-truth-cleanup` |
| Correct or simplify docs without behavior changes or source-of-truth conflict | `documentation-cleanup` |
| Security review, vulnerability audit, abuse path analysis | `security-codebase-audit` |
| Compliance, regulation, policy, privacy obligation, evidence gap review | `compliance-audit` |
| Refactor while preserving behavior | `refactoring` |
| Migrate old app, legacy system, or old architecture to a new target | `legacy-migration` |
| Upgrade framework, runtime, platform, or major library version | `framework-version-upgrade` |
| Review database schema, persistence boundaries, migrations, data access | `database-design-review` |
| Review API endpoints, request/response contracts, versioning, consumers | `api-design-review` |
| Map backend APIs to UI screens, data contracts, loading/error states | `backend-ui-integration-audit` |
| Prepare or assess release readiness | `release-readiness` |
| Review a PR, diff, patch, or proposed code change | `code-review` |
| Break work into reviewable PRs | `pull-request-planning` |
| Review UI, UX, accessibility, or design consistency | `ui-ux-review` |
| Design roles, permissions, access control, authorization model | `rbac-permission-design` |
| Design tenant isolation, shared resources, cross-tenant access boundaries | `multi-tenancy-design` |
| Build GTM strategy, launch motion, channel plan, positioning | `gtm-strategy` |
| Review fundraising narrative, pitch deck, investor story | `investor-pitch-review` |
| Design or evaluate testing approach, coverage model, risk-based testing | `testing-strategy` |
| Analyze outage, incident, degradation, near miss, production failure | `production-incident-analysis` |

## Safety-Sensitive Escalation

Apply these rules after selecting the likely primary workflow. These rules override generic repo, product, and business routing. They do not override an explicit valid workflow id from the user; in that case, keep the explicit workflow primary and add the safety workflow as secondary.

- If the task asks for a security audit or vulnerability review, primary workflow is `security-codebase-audit`.
- If the task asks for compliance, regulatory, privacy, or policy evidence review, primary workflow is `compliance-audit`.
- If the task asks for RBAC, authorization, permissions, roles, or access control design, primary workflow is `rbac-permission-design`.
- If the task asks for tenant isolation or cross-tenant data boundaries, primary workflow is `multi-tenancy-design`.
- If a code implementation touches authentication, authorization, secrets, crypto, payments, PII, tenant boundaries, file upload, command execution, dependency loading, or network calls, keep the implementation workflow primary and add the relevant safety workflow as secondary.
- If database work includes migrations, destructive schema changes, data backfills, or retention behavior, require migration and rollback thinking in the selected output contract.
- If production behavior, incident response, rollout, rollback, or release risk is central, add `release-readiness` or `production-incident-analysis` as a secondary workflow unless it is already primary.

## Repo and Codebase Routing

- Use `coding-implementation` for scoped code changes after repository inventory.
- Use `code-review` for diffs, patches, pull requests, or requested review comments.
- Use `full-codebase-audit` for broad repository audits across multiple concerns.
- Use `refactoring` only when behavior must be preserved and structure is the main concern.
- Use `legacy-migration` or `framework-version-upgrade` when old and new targets must coexist or compatibility matters.
- Use `documentation-source-of-truth-cleanup` when docs conflict; use `documentation-cleanup` when docs are merely stale, unclear, or verbose.
- Use `backend-ui-integration-audit` when backend and frontend contracts must be mapped together.
- Use `api-design-review` when the API contract itself is the object of review.
- Use `database-design-review` when persistence, schema, migration, or access pattern design is the object of review.
- Use `testing-strategy` when the task asks what to test; use the exact registry match for automation repository design when the task asks how to structure a test automation repo.

## Business and Product Routing

- Use product workflows when the task concerns customer problem, MVP scope, roadmap, feature gaps, product analytics, or AI product decisions.
- Use business workflows when the task concerns GTM, marketplace mechanics, pricing, monetization, or investor narrative.
- For product/business tasks not listed in the table, choose the single most specific registry workflow by matching the user object first, then the action.
- Do not route business or product tasks to codebase workflows unless the user asks to inspect or modify a repository.

## Ambiguous Task Fallback

Use `needs_clarification` only when a reasonable route would risk changing the wrong artifact, violating scope, or making an irreversible decision.

Otherwise resolve ambiguity deterministically:

- If the user asks for code changes in a repository but the domain is unclear, use `coding-implementation`.
- If the user asks for broad improvement without an artifact, use the registry default workflow sequence in `PLAN_ONLY`.
- If the user asks for "review this" and provides a diff or PR, use `code-review`.
- If the user asks for "review this" and provides a whole repo, use `full-codebase-audit`.
- If the user asks for "review this" and provides product or business prose, route by the closest product/business intent.
- If no artifact is available, state the assumption in the task intake card and keep the output non-destructive.

## Default Universal Workflow Behavior

Use the registry `default_workflow_sequence` when no exact workflow matches after applying the rules above.

Default behavior must:

- Preserve the user's stated scope.
- Start with inventory or task understanding before recommendations.
- Produce a task intake card.
- Select the closest available output contract.
- Avoid adding features, adapters, examples, tests, or architecture changes unless the user explicitly requested them.
