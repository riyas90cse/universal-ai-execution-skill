# Focused Security Audit Example

## User Request

"Audit the authorization and tenant isolation paths for this feature."

## Routing

- Primary workflow: `security-codebase-audit`
- Secondary lens: `multi-tenancy-design`
- Execution mode: `REVIEW`
- Optional focused skill: `skills/security/security-audit/SKILL.md`
- Output contract: Security Audit

## Expected Behavior

The router selects the security workflow and output contract. The focused skill then adds threat modeling, trust-boundary inventory, abuse-case tracing, calibrated severity, remediation, and verification guidance.

The audit should separate confirmed findings from hypotheses. It should cite concrete code, configuration, policy, or runtime evidence and name residual risk where evidence is missing.

## Good Prompt

"Trace whether users can access data outside their tenant. Cite files and call out confirmed findings separately from hypotheses."

## Bad Prompt

"Find all security problems in the app."
