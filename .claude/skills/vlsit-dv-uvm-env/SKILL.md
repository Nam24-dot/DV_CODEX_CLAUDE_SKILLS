---
name: vlsit-dv-uvm-env
description: "Build, extend or review reusable SystemVerilog UVM agents and environments. Use for interface, driver, monitor, sequencer, env, configuration, test and integration architecture."
---

# UVM Environment

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
DUT ports/interface contract, existing project/filelist and selected UVM implementation. Resolve clocks, resets and active/passive roles before driving signals.

## Workflow
1. Inspect repository conventions and installed simulator/UVM support. Select one compatible API baseline; do not mix legacy UVM 1.2 examples with unverified implementation-specific APIs.
2. Map agent instances and active/passive settings to interfaces. Define transaction types, configuration objects and virtual interface ownership; document pin-to-transaction mapping.
3. Define clocking/sampling, accepted-transfer event, backpressure and reset behavior before implementing driver and monitor. Drivers own stimulus; monitors independently reconstruct observed transactions.
4. Create components with factory registration and consistent constructors. Obtain configuration/virtual interfaces in build_phase with explicit failure on missing required configuration. Create/connect ports in appropriate phases.
5. Connect monitor analysis streams to scoreboard, coverage and optional RAL predictor. Preserve object ownership. Keep reference predictions independent of driver intent when acceptance matters.
6. Put test-level objections around bounded sequence execution and drain criteria. Include a watchdog, reset recovery and check_phase/report_phase checks for leftovers and activity.
7. Generate ordered filelists and discover actual build commands. Compile, elaborate, then run smoke and a backpressure/reset case where tools exist. Report each stage separately.

## Deliverables
Agent/environment source files, topology/connection map, ordered filelist, smoke test and integration report.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

Use [specialized contract](assets/architecture.md) to specify the implementation boundaries before coding.

## Detailed guidance
For implementation, review or closure beyond initial triage, read [detailed workflow](references/detailed-workflow.md). Use only the sections relevant to the requested scope.

Use [review-ledger.csv](assets/review-ledger.csv) when recording the detailed review.
