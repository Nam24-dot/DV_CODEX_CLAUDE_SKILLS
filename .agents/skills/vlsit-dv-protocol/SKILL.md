---
name: vlsit-dv-protocol
description: "Define and verify bus/interface contracts, channel timing, ordering and protocol checker coverage. Use for APB, AXI or ready/valid compliance; not general UVM scaffolding."
---

# Protocol Verification

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.


## Inputs
Authoritative protocol issue, endpoint roles, supported features, transaction schema, clocks/reset and project-specific ordering/latency constraints.

## Workflow
1. Freeze protocol variant and feature subset; separate normative protocol rules from implementation guarantees.
2. Define per-channel acceptance/stability and cross-channel transaction completion and ordering.
3. Build directed and randomized legal scenarios for channel timing, boundaries, backpressure, errors and reset.
4. Use protocol-specific matching and independent data checks; do not assume channel arrivals are simultaneous.
5. Demonstrate activation and controlled violation detection without weakening normal driver behavior.
6. Deliver clause-to-check/coverage traceability and explicit unsupported feature or conformance limits.

## Detailed guidance
Read [detailed procedure](references/task.md) for the selected review or execution stages. Do not load unrelated sibling workflows.

## Deliverables and completion
Use the [output template](assets/output-template.md) and the applicable ledgers below. Report artifact identities, executed checks, unexecuted checks, unresolved decisions and scoped delivery status. Templates are not completed evidence.

- [channels.csv](assets/channels.csv)
- [scenarios.csv](assets/scenarios.csv)

## VIP integration
For implementation-specific VIP APIs, wrappers, enables and compatibility, use `vlsit-dv-vip` when installed. Protocol-rule correctness and VIP integration are separate responsibilities; retain clause-to-check traceability.
