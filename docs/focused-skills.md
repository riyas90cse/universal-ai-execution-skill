# Focused Skills

Focused skills are optional execution accelerators for high-value workflows. The Universal AI Execution Skill remains the router and the workflow registry remains the source of truth for workflow definitions.

## Router Versus Focused Skills

- Router: `skills/universal-ai-execution/SKILL.md` classifies the task, selects the workflow, chooses the execution mode, applies the output contract, and enforces validation.
- Registry: `skills/universal-ai-execution/references/workflow-registry.yaml` defines the canonical workflow IDs and workflow content.
- Focused skills: `skills/**/SKILL.md` files provide deeper playbooks for selected workflow IDs after routing is complete.

If a mapped focused skill is unavailable, the router still works with the registry and output contracts alone.

## Mapping

The canonical mapping lives in `skills/universal-ai-execution/references/workflow-registry.yaml` under `focused_skill_mappings`.

The readable mapping table is generated into `skills/universal-ai-execution/references/technique-registry.md`. Do not copy the mapping into router, adapter, example, or README files; update the YAML source and regenerate the readable registry instead.

## Focused Skill Structure

Every focused skill should include:

- Purpose.
- Mapped workflows.
- When to use.
- Required inputs.
- Process.
- Output contract.
- Validation checklist.
- Common mistakes.

Focused skills may reference mapped workflow IDs, but they must not copy full workflow registry entries, workflow sequences, required outputs, validation rules, or common mistakes from the registry.

## Routing Behavior

1. Read the user request and repository instructions.
2. Use the universal router to classify the task and select the primary workflow.
3. Check `focused_skill_mappings` for an optional accelerator.
4. Load the focused skill only when it helps the selected workflow.
5. Apply the registry workflow and output contract as the authority.
6. Validate before claiming completion.

## Adding A Focused Skill

1. Choose existing workflow IDs from the registry.
2. Create a focused `SKILL.md` with the required sections.
3. Add mapping entries to `focused_skill_mappings`.
4. Keep workflow definitions in the registry.
5. Regenerate the readable registry if the generator renders the mapping.
6. Run repository validation.
