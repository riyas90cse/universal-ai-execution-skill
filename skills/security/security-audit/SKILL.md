---
name: security-audit
description: Review security-sensitive code, authorization models, and tenant boundaries through threat modeling and evidence-backed findings.
---

# Security Audit

## Purpose

Use this focused skill to audit security-sensitive systems, code paths, authorization models, or tenant isolation. It turns security workflows into a structured review with explicit assets, trust boundaries, abuse cases, findings, and verification steps.

## Mapped Workflows

- `security-codebase-audit`
- `rbac-permission-design`
- `multi-tenancy-design`
- `compliance-audit`

## When To Use

- The user asks for a security audit, vulnerability review, or abuse-case analysis.
- Code touches authentication, authorization, secrets, PII, payments, file upload, command execution, or network calls.
- Roles, permissions, or tenant isolation need design or review.
- Compliance evidence depends on security controls.

## Required Inputs

- Codebase, diff, design, policy, or architecture under review.
- Assets, actors, trust boundaries, and data sensitivity if known.
- Expected security properties or compliance obligations.
- Available tests, logs, configuration, and deployment context.

## Process

1. Inventory entry points, assets, trust boundaries, identities, privileges, and data flows.
2. Identify relevant abuse cases before listing findings.
3. Trace candidate issues from source to sink using repository evidence.
4. Calibrate severity by exploitability, impact, exposure, and compensating controls.
5. Separate confirmed findings from hypotheses and false positives.
6. Recommend remediations with verification steps and residual risk.

## Output Contract

Return a security audit with:

- Scope and excluded surfaces.
- Threat model.
- Findings with severity, affected surface, evidence, exploitability, impact, and remediation.
- False positives or hypotheses.
- Remediation plan.
- Verification plan.
- Residual risk.

## Validation Checklist

- Security claims cite concrete code, config, policy, or runtime evidence.
- Findings include plausible attack paths or abuse cases.
- Severity is calibrated, not alarmist.
- Remediation is specific enough to implement and verify.
- Unknowns and residual risks are explicit.

## Common Mistakes

- Reporting checklist items without attack paths.
- Treating theoretical issues as confirmed findings.
- Ignoring authorization and tenant boundaries in favor of generic dependency concerns.
- Recommending fixes without verification criteria.
