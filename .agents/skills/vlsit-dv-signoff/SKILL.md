---
name: vlsit-dv-signoff
description: "Audit requirement closure, regressions, coverage, waivers and remaining risks for verification handoff. Use for DV readiness reviews, milestone reports or sign-off recommendations."
---

# DV Sign-off Review

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Acceptance criteria, requirement matrix, run evidence, coverage reports, defect list, configuration inventory and waiver approvals.

## Workflow
1. Freeze the reviewed revisions and configuration set. Inventory required artifacts and thresholds from the project; if missing, produce a readiness review with acceptance blocked rather than inventing thresholds.
2. Reconcile every in-scope requirement with checker, stimulus, coverage and actual evidence. Flag stale evidence after RTL/TB/spec changes and missing configuration results.
3. Audit regression counts, unresolved failures, inconclusive formal properties, coverage denominators, exclusions, disabled checkers and checker activity.
4. Review defects by impact, reproduction and disposition. Require owner/rationale/evidence/expiry for waivers and distinguish technical pass from accepted risk.
5. Assess verification adequacy separately from numeric coverage. Identify unsupported tools/features, CDC/RDC/low-power/security scope and integration gaps when applicable.
6. Produce READY_FOR_REVIEW, NOT_READY or BLOCKED with explicit reasons. These are recommendations, not an autonomous human sign-off or tapeout authorization.
7. Preserve original required checks and failed evidence. List the smallest concrete actions to close each blocker and the person/role required for acceptance.

## Deliverables
dv_signoff_report.md, evidence index, rule/requirement matrices and open-risk/waiver ledger.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Additional assets
- Use [waivers.csv](assets/waivers.csv) for the corresponding task ledger.

## Detailed guidance
For implementation, review or closure beyond initial triage, read [detailed workflow](references/detailed-workflow.md). Use only the sections relevant to the requested scope.

Use [review-ledger.csv](assets/review-ledger.csv) when recording the detailed review.
