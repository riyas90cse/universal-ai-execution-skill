# Security Review Rules

This file defines security review guardrails. It does not add security workflows,
tools, or execution logic.

## Security Review Triggers

Apply these rules when work touches:

- Authentication, sessions, identity, login, logout, or account recovery.
- Authorization, RBAC, permissions, tenant isolation, or ownership checks.
- Public APIs, webhooks, callbacks, file uploads, or user-generated content.
- Secrets, credentials, tokens, encryption keys, or sensitive configuration.
- Personal, financial, regulated, or tenant-scoped data.
- Input validation, parsing, command execution, dependency loading, or network calls.
- Logging, monitoring, audit trails, or incident response behavior.

## Threat Model Minimum

For security-sensitive work, identify:

- Assets: data, credentials, actions, systems, and business processes at risk.
- Actors: anonymous user, authenticated user, tenant user, admin, service account, or third party.
- Trust boundaries: browser/server, tenant/tenant, user/admin, public/internal, app/dependency.
- Entry points: routes, APIs, jobs, uploads, imports, webhooks, and admin tools.
- Abuse cases: what an attacker tries to read, write, bypass, exhaust, or hide.

## Required Review Areas

| Area | Required checks |
| --- | --- |
| Authentication | Session validity, token lifetime, replay risk, password/account recovery paths |
| Authorization | Object-level checks, action-level checks, default deny behavior |
| RBAC | Role definitions, privilege escalation paths, least privilege, admin boundaries |
| Multi-tenancy | Tenant lookup, tenant-scoped queries, cross-tenant IDs, shared resources |
| File uploads | Type validation, size limits, storage path control, malware or active content risk |
| Public APIs | Authentication, rate limits, schema validation, error disclosure, versioning |
| Secrets | No hardcoded secrets, safe storage, redaction, rotation assumptions |
| Sensitive logging | No tokens, PII, credentials, tenant secrets, or regulated data in logs |
| Rate limiting | Abuse-prone endpoints, authentication endpoints, write actions, expensive reads |
| Audit logs | Security-relevant actions, actor, target, timestamp, outcome, tamper resistance |
| Tenant isolation | Query filters, storage prefixes, cache keys, background jobs, exports |
| Input validation | Server-side validation, canonicalization, allowlists, parser failure behavior |
| Dependency risk | New dependency need, maintenance, license, known vulnerabilities, transitive risk |

## Positive and Negative Tests

- Positive tests prove authorized users can perform intended actions.
- Negative tests prove unauthorized users, wrong roles, wrong tenants, invalid inputs, and expired credentials are denied.
- Security fixes should include at least one negative test or a clear manual abuse-case check.
- Do not treat UI hiding as authorization.
- Do not treat client-side validation as sufficient input validation.

## Severity Calibration

Use concrete impact:

- Critical: remote code execution, credential compromise, broad tenant/data exposure, auth bypass for privileged actions.
- High: unauthorized sensitive data access, privilege escalation, write access across trust boundaries.
- Medium: limited data exposure, missing rate limit on abuse-prone endpoint, incomplete audit trail for sensitive action.
- Low: hardening gap with low exploitability or limited impact.

## Security Review Output

Report:

- Scope and trust boundaries reviewed.
- Findings with severity, evidence, impact, and remediation.
- Abuse cases tested or reason they could not be tested.
- Residual risk and follow-up constraints.
- Validation performed, including negative tests or manual checks.
