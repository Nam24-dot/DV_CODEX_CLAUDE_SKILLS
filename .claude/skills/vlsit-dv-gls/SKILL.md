---
name: vlsit-dv-gls
description: "Prepare, review and debug gate-level simulation with netlist libraries, SDF annotation, timing checks and X tracing. Use for GLS or post-synthesis/post-layout simulation; not STA or equivalence sign-off."
---

# Gate-Level Simulation

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.


## Inputs
Netlist/top, matched simulation libraries and macros, optional SDF, clock/reset/mode contract, simulator/version and required corner/scenario matrix.

## Workflow
1. Select PRE_SYNTH (after synthesis, no SDF), POST_PNR (after place and route, no SDF), or POST_PNR_SDF (after place and route with SDF). Read the [three-phase methodology](references/phases.md), then freeze phase-specific artifact identities and required modes.
2. Resolve library cells, macro models, hierarchy and reset initialization before relying on functional results.
3. For POST_PNR_SDF, audit SDF root, corner, min/typ/max selection, precision, annotated/unmatched/rejected scope and diagnostics. For the two no-SDF phases, record the actual library delay model and timing-check settings.
4. Run representative reset/traffic/clock scenarios with active checking and inspect timing violations and earliest X sources.
5. Keep diagnostic suppressions separate from acceptance runs; preserve original timing failures and annotation gaps.
6. Deliver corner/mode results and scoped exceptions; do not infer STA, equivalence or DFT completion from GLS.

## Detailed guidance
Read [detailed procedure](references/task.md) for the selected review or execution stages. For tool compatibility, read [source guidance](references/sources.md). Do not load unrelated sibling workflows.

## Deliverables and completion
Use the [output template](assets/output-template.md) and the applicable ledgers below. Report artifact identities, executed checks, unexecuted checks, unresolved decisions and scoped delivery status. Templates are not completed evidence.

- [annotation.csv](assets/annotation.csv)
- [scenarios.csv](assets/scenarios.csv)
- [violations.csv](assets/violations.csv)
