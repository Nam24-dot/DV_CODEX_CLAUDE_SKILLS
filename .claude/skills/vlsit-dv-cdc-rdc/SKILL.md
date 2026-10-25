---
name: vlsit-dv-cdc-rdc
description: "Review clock/reset crossing constraints, reports, synchronization protocols and waivers. Use for CDC or RDC analysis; digital simulation alone does not prove metastability safety."
---

# CDC and RDC Verification

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.


## Inputs
RTL/netlist, clocks/resets and mode definitions, tool/version, constraints, crossing reports and current waiver/evidence set.

## Workflow
1. Audit clock/reset/mode coverage and record unconstrained or abstracted objects before evaluating violation counts.
2. Classify single-bit, pulse, handshake, multi-bit, FIFO and reconvergent crossings by actual protocol.
3. Analyze reset-domain effects separately, including independent reset with a shared clock.
4. Triage findings using structural and functional evidence; correct setup errors before rerunning.
5. Check data/event integrity and reset recovery with available dynamic/formal tools; retain analog/physical limitations.
6. Deliver crossing and constraint ledgers with scoped reviewed waivers and unresolved risks.

## Detailed guidance
Read [detailed procedure](references/task.md) for the selected review or execution stages. Do not load unrelated sibling workflows.

## Deliverables and completion
Use the [output template](assets/output-template.md) and the applicable ledgers below. Report artifact identities, executed checks, unexecuted checks, unresolved decisions and scoped delivery status. Templates are not completed evidence.

- [crossings.csv](assets/crossings.csv)
- [constraints.csv](assets/constraints.csv)
- [waivers.csv](assets/waivers.csv)
