# Product and Business Review Rules

This file defines guardrails for product and business critique. It does not add
workflows or execution logic.

## Core Rules

- Prove the problem before expanding the solution.
- Separate buyer, user, evaluator, and administrator when they differ.
- Treat enthusiasm, internal preference, and feature count as weak evidence.
- Do not recommend building before naming the riskiest assumption.
- Prefer small validation experiments over large speculative scope.

## Required Review Questions

| Area | Required questions |
| --- | --- |
| ICP | Who is the narrow initial customer profile, and what excludes others for now? |
| Pain | What specific problem occurs, how often, and what it costs today? |
| Urgency | Why must this be solved now instead of later? |
| Willingness to pay | Who pays, what budget exists, and what current spend or workaround proves value? |
| Competition | What alternatives exist, including spreadsheets, manual work, agencies, or doing nothing? |
| Distribution | How will the target customer be reached repeatedly and affordably? |
| MVP proof | What smallest proof would show the core risk is real? |
| Scope cut | Which features can be removed without invalidating the learning goal? |
| Validation experiments | What experiment, signal, and decision threshold will prove or disprove the assumption? |
| Buyer vs user | Who approves, who uses, who blocks, and whose pain drives adoption? |
| Proof before building | What evidence is required before code, design, hiring, or GTM spend expands? |

## Evidence Standards

Strong evidence includes:

- Customer interviews with repeated pain patterns.
- Existing spend, budget, or paid pilots.
- Manual workflows users already perform despite friction.
- High-intent waitlists, usage, retention, conversion, or expansion signals.
- Competitive displacement or documented dissatisfaction with alternatives.

Weak evidence includes:

- "Everyone needs this" claims.
- Compliments without commitment.
- Large market size without reachable wedge.
- Feature requests without urgency or budget.
- Internal excitement without external proof.

## Scope Cut Rules

- Keep only features that test the main risk or deliver the first paid/useful outcome.
- Defer polish, automation, integrations, and admin controls unless they are required for the test.
- Do not build multi-segment support before one segment is proven.
- Do not build marketplace supply and demand depth before validating the constrained wedge.
- State non-goals explicitly so they do not re-enter as hidden scope.

## Validation Experiment Rules

Each experiment must name:

- Assumption being tested.
- Target participant or customer.
- Method: interview, concierge test, landing page, prototype, paid pilot, manual service, pricing test, or usage test.
- Success threshold.
- Failure threshold or stop condition.
- Time box.
- Next decision if the threshold is met or missed.

## Business Risk Checks

Review:

- Acquisition channel cost and repeatability.
- Sales cycle length and buyer complexity.
- Price relative to urgency and alternative cost.
- Operational burden of delivering the promise.
- Competitive response and differentiation durability.
- Legal, compliance, security, or trust blockers.

## Output Rules

Report:

- ICP, buyer, user, and pain in separate lines.
- Riskiest assumptions ranked by impact.
- Evidence found and evidence missing.
- Recommended scope cut.
- Validation experiment with threshold and stop condition.
- Decision: build, test first, narrow scope, or stop.
