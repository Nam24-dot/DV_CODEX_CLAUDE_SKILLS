---
name: vlsit-dv-testplan
description: "Turn RTL specifications and interface/register contracts into risk-ranked verification plans and requirement traceability matrices. Use for test planning, corner-case analysis or verification impact of specification changes."
---

# DV Test Plan

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Specification or user-described behavior; optional RTL/TB, interface manuals, register maps and acceptance criteria. Without a spec produce a clearly marked inferred plan.

## Workflow
1. Extract atomic requirements with source sections and stable IDs. Separate normative behavior, inferred behavior, assumptions and unresolved contradictions.
2. Inventory interfaces, operating modes, parameter limits, clocks, resets, interrupts, register side effects, throughput/latency and illegal-operation policies.
3. For every requirement define a scenario, independent checking strategy, observable event, functional/assertion coverage target and acceptance evidence. Include priority and owner.
4. Cover nominal and boundary behavior, stalls/backpressure, concurrent operations, reset during traffic, error propagation, recovery and configuration interactions. Do not assert specific protocol behavior without identifying the protocol/version.
5. Choose directed, constrained-random, assertion and formal techniques by risk. Distinguish required checks from optional improvements and state resource assumptions.
6. Review uncovered requirements and uncheckable requirements separately. For changes, map added/modified/retired requirements to affected tests, checkers and bins; preserve historical IDs.

## Deliverables
verification_plan.md, requirements.csv, open_questions.md and configuration/test matrix.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Additional assets
- Use [requirements.csv](assets/requirements.csv) for the corresponding task ledger.

## Detailed guidance
For implementation, review or closure beyond initial triage, read [detailed workflow](references/detailed-workflow.md). Use only the sections relevant to the requested scope.

Use [review-ledger.csv](assets/review-ledger.csv) when recording the detailed review.
