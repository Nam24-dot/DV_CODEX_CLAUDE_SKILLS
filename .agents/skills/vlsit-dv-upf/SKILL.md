---
name: vlsit-dv-upf
description: "Review IEEE 1801 UPF and verify power states, isolation, retention and power-aware recovery. Use for low-power intent and simulation; not power estimation or physical implementation sign-off."
---

# UPF and Low-Power Verification

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.


## Inputs
Power architecture, selected UPF edition/files/load order, RTL or netlist, simulator support, supply/state model and power/reset/clock sequencing contract.

## Workflow
1. Inventory domains, supplies, switches, control ownership and legal states against the selected UPF edition.
2. Inspect resolved intent, element membership, strategy binding and simulator feature support.
3. Derive legal transition partial orders and in-flight traffic handling from the design specification.
4. Check isolation at live receiver boundaries, retained versus non-retained state and wake-up/reset recovery.
5. Cover observed states/transitions and interactions; demonstrate checker sensitivity with scoped fault variants where supported.
6. Report static, dynamic and implementation evidence separately, retaining unsupported features and unresolved bindings.

## Detailed guidance
Read [detailed procedure](references/task.md) for the selected review or execution stages. For failures and version-sensitive commands, read [debug and source guidance](references/debug.md). Do not load unrelated sibling workflows.

## Deliverables and completion
Use the [output template](assets/output-template.md) and the applicable ledgers below. Report artifact identities, executed checks, unexecuted checks, unresolved decisions and scoped delivery status. Templates are not completed evidence.

- [domains.csv](assets/domains.csv)
- [transitions.csv](assets/transitions.csv)
- [strategies.csv](assets/strategies.csv)
