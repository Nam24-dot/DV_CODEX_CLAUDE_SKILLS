---
name: vlsit-dv-sva-formal
description: "Develop and review SystemVerilog Assertions and formal harnesses. Use for protocol properties, invariants, bounded liveness, formal assumptions, vacuity or counterexample analysis."
---

# SVA and Formal

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Requirements, signal/clock/reset map, assertion support and optional formal flow. Require explicit interface environment constraints and proof scope.

## Workflow
1. Translate each requirement to an observable property and classify safety, bounded response, liveness or cover. Define the triggering event and timing in cycles.
2. Select sampling clock and reset disable behavior. Document overlapped versus non-overlapped implication and history requirements; guard $past after initialization/reset where needed.
3. Separate DUT assertions from environment assumptions. Do not assume away DUT errors, backpressure, reset or legal corner cases. Document fairness only when justified by the environment contract.
4. Add activation covers or equivalent analysis to identify vacuous properties. Test legal traces and deliberate violations; a property that never triggers is not useful checking evidence.
5. Bind without modifying functional RTL where appropriate. Ensure signals, widths, parameters and generated instance scopes resolve across required configurations.
6. For formal, inspect reachability, constraint consistency, black boxes, abstractions and reset initialization. Record property-level proof type, depth and assumptions.
7. Classify timeout/unknown as INCONCLUSIVE. Preserve counterexamples; distinguish a real design violation from an incorrect property/harness. Never describe a bounded proof as universal correctness.

## Deliverables
Assertion/bind files or formal harness, property matrix, assumption ledger and execution/counterexample report.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Additional assets
- Use [properties.csv](assets/properties.csv) for the corresponding task ledger.

## Detailed guidance
For implementation, review or closure beyond initial triage, read [detailed workflow](references/detailed-workflow.md). Use only the sections relevant to the requested scope.

Use [review-ledger.csv](assets/review-ledger.csv) when recording the detailed review.
