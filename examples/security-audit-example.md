# Security Audit Example

## User Request

"Audit the authentication and file upload paths for security risks. Show real evidence, abuse cases, and a remediation plan."

## Detected Task Type

Security codebase audit for sensitive entry points.

## Selected Workflow

`security-codebase-audit`

## Why This Workflow Was Selected

The request explicitly asks for security review, abuse paths, and remediation priorities.

## Expected Output Structure

- Task intake card with security scope and excluded surfaces.
- Asset inventory and trust boundaries.
- Threat model with actors and abuse cases.
- Findings with severity, evidence, exploitability, impact, and remediation.
- False positives or hypotheses separated from confirmed issues.
- Remediation plan and verification plan.
- Residual risk.

## Good Prompt

"Review authentication and file uploads for security issues. Trace findings to code, include abuse cases and severity, and propose verification steps for each fix. Do not report generic best practices without evidence."

## Bad Prompt To Avoid

"Make the app secure and upgrade any security-related packages you find."
