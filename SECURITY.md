# Security Policy

## Supported Versions

The project is preparing its first public release. Until versioned releases exist, security fixes apply to the active `main` branch.

After versioned releases begin, supported versions will be documented here and in the changelog.

## Scope

This repository contains documentation, a portable Agent Skill, workflow registry data, adapters, examples, tests, and validation scripts.

Security reports may include:

- Unsafe guidance in security-sensitive workflow rules.
- Incorrect claims that could cause unsafe AI-assisted changes.
- Validation gaps that allow registry or router drift.
- Issues in repository scripts or CI configuration.

This project does not run a hosted service and does not process user data.

## Reporting a Vulnerability

Please do not report security vulnerabilities in public issues.

Use GitHub private vulnerability reporting if it is available for this repository. If it is not available, contact the maintainers through GitHub with a brief summary and steps to reproduce.

Please include:

- Affected file or area.
- Impact and realistic abuse case.
- Steps to reproduce or validate the issue.
- Suggested mitigation, if known.

## Response Expectations

Maintainers will review valid reports and coordinate a fix before public disclosure when appropriate.

Security fixes should include validation steps and should not broaden scope beyond the confirmed issue.

## Limitations

The Universal AI Execution Skill improves review discipline, but it does not guarantee security, correctness, or compliance. Human review remains required for sensitive changes.
