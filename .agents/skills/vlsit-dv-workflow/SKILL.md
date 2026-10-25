---
name: vlsit-dv-workflow
description: "Coordinate block or subsystem Design Verification from specification through planning, UVM, assertions, regression and evidence-based handoff. Use for end-to-end DV tasks or selecting the appropriate DV skill."
---

# DV Workflow

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Project/spec location, DUT boundary and desired milestone. Discover existing tools and verification assets before proposing replacements.

## Workflow
1. Inventory the supplied project and read its instructions. Record current revisions and available specifications, TB architecture, run targets and unresolved questions.
2. Create a scoped work plan and requirement ledger. Route specification analysis to dv-testplan; environment to dv-uvm-env; stimulus to dv-sequences; prediction to dv-scoreboard; properties to dv-sva-formal; coverage to dv-coverage; registers to dv-ral; execution to dv-regression; failures to dv-debug; netlist/SDF checks to dv-gls; power intent to dv-upf; clock/reset crossings to dv-cdc-rdc; protocol compliance to dv-protocol; handoff to dv-signoff.
3. Load only the selected sibling skills. If a sibling is not installed, report it as unavailable and perform only the supported portion; do not invent its contents.
4. Establish dependency order: requirements before expected behavior; monitor acceptance contract before scoreboard/coverage; compile before simulation; representative smoke before broad regression; credible evidence before sign-off.
5. Continue implementation and available checks within the user's authorization. Isolate unanswered semantic decisions; do not block independent work or impose a blanket approval gate.
6. Keep a milestone ledger: planned, implemented, checked, blocked. Reconcile failures and changed requirements before final handoff.

## Deliverables
dv_work_plan.md, requirement ledger, artifact/evidence index and milestone summary.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Detailed guidance
For implementation, review or closure beyond initial triage, read [detailed workflow](references/detailed-workflow.md). Use only the sections relevant to the requested scope.

Use [review-ledger.csv](assets/review-ledger.csv) when recording the detailed review.
