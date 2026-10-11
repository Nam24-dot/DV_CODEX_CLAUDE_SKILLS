---
name: vlsit-dv-sequences
description: "Create directed and constrained-random UVM sequences, tests and scenario matrices. Use for stimulus generation, corner cases, concurrency, stress, error injection or randomization debugging."
---

# DV Stimulus

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Verification plan, transaction constraints, sequencer/driver API, supported modes and reset contract.

## Workflow
1. Map planned scenarios to requirement IDs. Separate legal stimulus, software misuse and deliberate electrical/protocol violations.
2. Define legal ranges and relations with width/signedness awareness. Include minimum/maximum, alignment, masks, burst limits, data patterns and concurrent activity required by the contract.
3. Implement composable directed sequences before random mixing. Use virtual sequences only when coordinating multiple sequencers/interfaces is needed.
4. Check every randomize() return; terminate with actionable diagnostics on unsatisfied legal constraints. Control distributions deliberately and prove required corners remain reachable.
5. Make delay, backpressure, reset and error scenarios bounded and reproducible. Define outstanding-transaction limits, response collection and cancellation behavior.
6. Record actual seed and configuration from the simulator. Check generated/accepted/completed transaction counts rather than assuming requested stimulus reached the DUT.
7. Run focused scenarios and inspect checker/coverage activation before increasing seed count. Retain failing seeds and avoid seed shopping.

## Deliverables
Sequence/test classes, scenario matrix, seed/configuration manifest and executed-check report.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.
