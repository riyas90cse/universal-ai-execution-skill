# Output Contracts

This file defines structured output formats for the Universal AI Execution Skill.
It does not define workflow steps or duplicate the workflow registry.

Source of truth:

- Workflow definitions: `workflow-registry.yaml`
- Classification rules: `task-classification-rules.md`
- Router entrypoint: `../SKILL.md`

## Shared Contract Rules

- Use the selected contract plus the task intake card for substantial workflow outputs.
- Use only execution modes defined in `../SKILL.md`: `ANALYZE_ONLY`, `PLAN_ONLY`, `IMPLEMENT`, `REVIEW`, `ORCHESTRATE`, and `VALIDATE`.
- Keep assumptions separate from evidence.
- Mark unknown or uninspected information as `Unknown` or `Not inspected`.
- Do not claim validation unless the validation was actually performed.
- For codebase work, cite concrete files, modules, commands, diffs, or repository evidence.
- For findings, include severity, evidence, impact, and recommendation.
- For plans, include scope boundaries, ordered steps, dependencies, risks, and validation.
- Omit sections only when the contract marks them optional or the user explicitly requests a shorter format.

## Execution Mode Constraints

- `ANALYZE_ONLY`: report observations, evidence, and conclusions without proposing an implementation plan unless requested.
- `PLAN_ONLY`: provide ordered steps and validation criteria without claiming changes were made.
- `IMPLEMENT`: include inventory, change summary, files changed, and validation result.
- `REVIEW`: lead with findings, risks, gaps, and evidence.
- `ORCHESTRATE`: include sequencing, ownership areas, dependencies, and handoff criteria.
- `VALIDATE`: include checks performed, results, failures, and remaining uncertainty.

## Contract Selection

| Workflow intent | Output contract |
| --- | --- |
| Initial classification or any substantial workflow | Task Intake Card |
| Full repository audit | Codebase Audit |
| Scoped code change planning or implementation | Implementation Plan |
| Security audit or abuse-case review | Security Audit |
| Compliance, policy, privacy, or regulatory review | Compliance Audit |
| Testing approach or coverage design | Testing Strategy |
| Backend/API to UI contract mapping | Backend/UI Integration Audit |
| Behavior-preserving structural change | Refactor Plan |
| Legacy migration, framework upgrade, cloud migration, cutover planning | Migration Plan |
| Documentation cleanup or source-of-truth reconciliation | Documentation Cleanup |
| Architecture, API, database, or major technical decision | Architecture Decision |
| Product idea, MVP, roadmap, or feature validation | Product Validation |
| GTM, launch, channel, marketplace, pricing, or positioning strategy | GTM Strategy |
| Release readiness or launch gate review | Release Readiness |
| Pull request, diff, patch, or proposed code review | Code Review |
| Pull request sequencing and reviewable change breakdown | PR Plan |
| Production incident, outage, degradation, or near miss | Incident Analysis |

## Task Intake Card

Required fields:

- `Task type`: normalized task category.
- `Selected workflow`: primary workflow id.
- `Execution mode`: one supported execution mode.
- `Scope`: included work and explicit non-goals.
- `Source of truth`: user request, issue, files, diff, registry, policy, logs, or other inspected material.
- `Assumptions`: assumptions needed to proceed.
- `Risks`: known routing, implementation, validation, safety, or scope risks.
- `Expected output`: selected contract and expected deliverable shape.

## Codebase Audit

Required sections:

- `Scope`: repository areas included, excluded, and why.
- `Inventory`: major modules, entry points, data stores, integrations, tests, and operational surfaces inspected.
- `Capability map`: user-facing or system capabilities mapped to implementation areas.
- `Findings`: severity, area, evidence, impact, and recommendation.
- `Gaps`: missing behavior, missing evidence, weak ownership, or unclear boundaries.
- `Prioritized roadmap`: ordered remediation or follow-up items with rationale.
- `Validation notes`: commands run, files inspected, and unvalidated areas.

## Implementation Plan

Required sections:

- `Problem statement`: current behavior, desired behavior, and issue boundary.
- `Repository inventory`: files, modules, tests, and contracts inspected before editing.
- `Change plan`: ordered small steps with expected files or components.
- `Scope controls`: explicit non-goals and avoided adjacent changes.
- `Risk review`: compatibility, data, security, UX, performance, or rollout risks.
- `Validation plan`: tests, checks, manual verification, or reason validation is unavailable.
- `Completion output`: files changed, behavior changed, and validation result when implementation occurs.

## Security Audit

Required sections:

- `Scope`: assets, trust boundaries, entry points, and excluded surfaces.
- `Threat model`: actors, assets, abuse cases, and assumptions.
- `Findings`: severity, affected surface, evidence, exploitability, impact, and remediation.
- `False positives or hypotheses`: items reviewed but not confirmed.
- `Remediation plan`: ordered fixes with owner or area when known.
- `Verification plan`: how each fix should be tested or proven.
- `Residual risk`: accepted risks, unknowns, and follow-up questions.

## Compliance Audit

Required sections:

- `Scope`: product, data, region, policy, or regulation boundary.
- `Obligation map`: applicable obligations and the system behavior they affect.
- `Evidence inventory`: files, controls, logs, docs, or processes inspected.
- `Gap report`: obligation, current evidence, missing evidence, risk, and recommended remediation.
- `Uncertainty`: legal, policy, or implementation unknowns.
- `Remediation roadmap`: ordered actions with priority and validation evidence needed.
- `Non-legal note`: clarify when the output is technical analysis rather than legal advice.

## Testing Strategy

Required sections:

- `Scope`: feature, repository, product area, or release under test.
- `Risk model`: critical user paths, failure modes, and change-sensitive areas.
- `Current coverage`: existing tests, checks, fixtures, environments, and gaps.
- `Target strategy`: unit, integration, end-to-end, manual, exploratory, performance, or security coverage as relevant.
- `Prioritized gaps`: missing tests ranked by risk and effort.
- `Execution plan`: where tests should live, when they run, and how failures are handled.
- `Validation criteria`: measurable readiness or coverage signals.

## Backend/UI Integration Audit

Required sections:

- `Scope`: backend endpoints, UI screens, states, and user flows inspected.
- `Backend inventory`: endpoints, payloads, auth, errors, pagination, and side effects.
- `UI inventory`: screens, components, data needs, loading states, empty states, and error states.
- `Contract map`: UI need mapped to backend request, response, and state handling.
- `Gaps`: missing endpoints, mismatched fields, stale assumptions, or unhandled states.
- `PR-by-PR plan`: reviewable change order with dependencies.
- `Validation plan`: contract tests, UI checks, mock updates, or manual flows.

## Refactor Plan

Required sections:

- `Current behavior`: behavior that must be preserved.
- `Pain points`: structural issues with evidence.
- `Refactor boundary`: included modules, excluded modules, and stop conditions.
- `Proposed shape`: target structure, ownership, and dependency direction.
- `Migration steps`: incremental changes that keep the system working.
- `Risk controls`: tests, feature flags, compatibility shims, or rollback path.
- `Validation plan`: before-and-after checks proving behavior preservation.

## Migration Plan

Required sections:

- `Current state`: legacy system, framework, version, or environment inventory.
- `Target state`: destination architecture, version, platform, or behavior.
- `Compatibility requirements`: data, API, UI, operational, and user-facing continuity needs.
- `Gap analysis`: breaking changes, missing features, dependency risks, and operational risks.
- `Phased plan`: ordered migration phases with rollback or contingency.
- `Cutover plan`: release, monitoring, communication, and ownership steps.
- `Validation plan`: tests, smoke checks, data verification, and production readiness signals.

## Documentation Cleanup

Required sections:

- `Scope`: documentation files, audiences, and excluded content.
- `Source-of-truth map`: authoritative files or code paths for each documented claim.
- `Issues found`: stale, duplicate, conflicting, missing, or unclear content.
- `Cleanup plan`: ordered edits with rationale.
- `Change summary`: docs changed and intent of each change.
- `Validation`: source files checked, links checked, generated docs regenerated, or reasons checks were not run.
- `Future candidates`: optional out-of-scope docs to revisit later.

## Architecture Decision

Required sections:

- `Context`: problem, constraints, current system, and decision drivers.
- `Options considered`: viable options and rejected options.
- `Decision`: chosen option and why it fits current constraints.
- `Tradeoffs`: benefits, costs, risks, and operational impact.
- `Interfaces and boundaries`: APIs, data boundaries, ownership, and integration points.
- `Migration or rollout`: steps needed to adopt the decision safely.
- `Validation`: proof points, tests, review gates, or monitoring signals.

## Product Validation

Required sections:

- `Customer and problem`: target user, pain, urgency, and context.
- `Hypothesis`: value proposition, user behavior, and business assumption being tested.
- `Evidence`: known facts, signals, research, data, or gaps.
- `Riskiest assumptions`: assumptions ranked by potential to invalidate the idea.
- `Validation plan`: tests, interviews, landing pages, prototypes, metrics, or decision thresholds.
- `Scope recommendation`: MVP, non-goals, and learning milestones when relevant.
- `Next actions`: ordered steps and stop/go criteria.

## GTM Strategy

Required sections:

- `Target segment`: buyer, user, market, and initial wedge.
- `Positioning`: category, promise, differentiation, and proof points.
- `Channel strategy`: acquisition channels, sales motion, partnerships, or launch paths.
- `Offer and packaging`: pricing, packaging, activation, or marketplace mechanics when relevant.
- `Risks and assumptions`: demand, competition, economics, and execution risks.
- `Validation plan`: experiments, metrics, timelines, and decision thresholds.
- `Action plan`: ordered launch or GTM steps.

## Release Readiness

Required sections:

- `Release scope`: features, fixes, migrations, and excluded changes.
- `Readiness checklist`: product, engineering, testing, security, compliance, docs, support, and operations status.
- `Blocking issues`: severity, owner or area, evidence, and required resolution.
- `Risk assessment`: rollout, rollback, data, performance, dependency, and user impact risks.
- `Validation evidence`: tests, checks, approvals, monitoring, and manual verification.
- `Go/no-go decision`: decision, rationale, and conditions.
- `Rollback and monitoring`: rollback path, alerts, dashboards, and post-release checks.

## Code Review

Required sections:

- `Scope`: diff, PR, commit, files, or patch reviewed.
- `Summary`: brief description of the change under review.
- `Findings`: severity, file or area, evidence, impact, and recommended fix.
- `Questions`: blocking or non-blocking questions for the author.
- `Test gaps`: missing or weak validation.
- `Positive notes`: optional, only when useful and specific.
- `Verdict`: approve, request changes, comment only, or not enough information.

## PR Plan

Required sections:

- `Goal`: end state and boundaries of the larger change.
- `Inventory`: affected areas, dependencies, owners, and constraints.
- `PR sequence`: ordered PRs with purpose, files or areas, dependencies, and validation.
- `Review strategy`: which PRs need specialist review and why.
- `Risk controls`: feature flags, compatibility, rollback, data handling, and communication.
- `Out of scope`: deferred work and future issues.
- `Completion criteria`: what proves the sequence is done.

## Incident Analysis

Required sections:

- `Incident summary`: impact, timeline, affected users, and current status.
- `Detection and response`: how the issue was found, mitigated, and communicated.
- `Root cause analysis`: confirmed causes, contributing factors, and rejected hypotheses.
- `Blast radius`: systems, data, users, and operational processes affected.
- `Remediation`: immediate fixes and long-term prevention.
- `Validation`: proof the incident is resolved and monitoring in place.
- `Follow-up actions`: owners or areas, priority, and due criteria when known.
