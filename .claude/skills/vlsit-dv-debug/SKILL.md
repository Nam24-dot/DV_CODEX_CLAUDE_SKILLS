---
name: vlsit-dv-debug
description: "Diagnose simulation, UVM, assertion and scoreboard failures using reproducible evidence. Use for failing seeds, hangs, mismatches, races, reset bugs or simulator/elaboration errors."
---

# DV Failure Debug

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Failure log and reproducible command or run manifest; optional RTL/TB/spec/waveform. With logs only, give hypotheses and exact evidence needed rather than a confirmed root cause.

## Workflow
1. Preserve the original run, seed, source/configuration and first failure. Check whether the failure occurred during build, initialization, stimulus, checking, drain or infrastructure.
2. Reproduce using the same tool version and inputs when possible. Identify the earliest divergence instead of treating cascaded errors as independent root causes.
3. Trace expected and observed behavior back to the specification, monitor sampling and checker implementation. Inspect reset epochs, transaction ownership, widths, signedness and ID/order handling.
4. For hangs inspect objections, blocked waits, outstanding requests, sequencer-driver handshakes and clock/reset activity; add bounded diagnostic instrumentation rather than disabling the watchdog.
5. Rank DUT, testbench, specification, tool and infrastructure hypotheses with supporting and contradicting evidence. Reduce the failing case without discarding the triggering behavior.
6. Propose and implement only the in-scope fix. If RTL changes are outside the request, present the concrete finding/patch proposal and ask before changing behavior. Do not weaken checking to hide the symptom.
7. Rerun the original reproducer and a focused nearby regression. Preserve pre-fix failure and post-fix evidence; mark unexecuted fixes as unverified.

## Deliverables
Root-cause report, minimal reproducer or reproduction instructions, scoped fix and regression evidence.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Detailed guidance
For implementation, review or closure beyond initial triage, read [detailed workflow](references/detailed-workflow.md). Use only the sections relevant to the requested scope.

Use [review-ledger.csv](assets/review-ledger.csv) when recording the detailed review.
