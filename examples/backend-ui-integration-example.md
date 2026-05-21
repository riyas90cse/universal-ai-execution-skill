# Backend/UI Integration Example

## User Request

"Check whether the account settings UI is fully wired to the backend APIs. Identify missing fields, broken states, and the smallest PR sequence to finish the integration."

## Detected Task Type

Backend and frontend contract alignment audit.

## Selected Workflow

`backend-ui-integration-audit`

## Why This Workflow Was Selected

The request asks to map UI screens to backend endpoints and detect partial or missing integration.

## Expected Output Structure

- Task intake card with included screens and endpoints.
- Backend endpoint inventory.
- UI screen inventory.
- Contract map from UI needs to API requests and responses.
- Gap report for missing endpoints, fields, loading states, empty states, and error states.
- PR-by-PR integration plan.
- Validation plan for contract and UI checks.

## Good Prompt

"For the account settings flow, map each UI field and state to the backend contract. List missing or mismatched fields, loading/error gaps, and a small PR sequence. Do not redesign the UI."

## Bad Prompt To Avoid

"Fix the whole settings area and improve the dashboard while you are there."
