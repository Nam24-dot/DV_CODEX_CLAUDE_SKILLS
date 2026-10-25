---
name: vlsit-dv-scoreboard
description: "Build or debug independent reference models and transaction scoreboards. Use for expected-versus-observed checking, ordering, latency, data integrity, reset flush or outstanding transaction accounting."
---

# DV Scoreboard

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Behavioral specification, monitor transaction schema, ordering/latency contract and reset policy. Resolve ambiguous simultaneous-event precedence before coding affected prediction.

## Workflow
1. Define the oracle from requirements rather than DUT internals. State arithmetic precision, signedness, overflow, byte ordering, masks and unknown-value rules.
2. Drive the model from accepted inputs and compare at specified output completion events. Define same-cycle input/output ordering explicitly.
3. Select FIFO matching only for guaranteed in-order behavior; otherwise match by protocol IDs plus ordering domain/epoch. Handle multiple outstanding requests and ID reuse.
4. Detect unexpected, missing, duplicate and mismatched responses. Bound pending lifetime only where the contract permits a latency bound; otherwise use a separate test watchdog without inventing a DUT deadline.
5. Define flush/retain/cancel behavior on reset. Quarantine old-epoch traffic and avoid treating reset-cancelled transfers as valid successful comparisons.
6. Clone/copy retained transactions and check copy semantics. Avoid blocking operations inside analysis write functions; use queues/FIFOs and processing tasks where necessary.
7. Unit-check the model with known vectors and inject a controlled mismatch or dropped/duplicate transaction to demonstrate checker sensitivity. Inspect pending entries at test end.

## Deliverables
Reference model/scoreboard, matching/reset contract, checker sensitivity evidence and mismatch report format.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

Use [specialized contract](assets/model-contract.md) to specify the implementation boundaries before coding.

## Detailed guidance
For implementation, review or closure beyond initial triage, read [detailed workflow](references/detailed-workflow.md). Use only the sections relevant to the requested scope.

Use [review-ledger.csv](assets/review-ledger.csv) when recording the detailed review.
