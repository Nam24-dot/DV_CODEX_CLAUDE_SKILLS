---
name: vlsit-dv-coverage
description: "Define functional/assertion coverage and analyze coverage gaps against requirements. Use for covergroups, crosses, coverage merging, unreachable bins, exclusions or targeted closure plans."
---

# DV Coverage Closure

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Requirement/test plan, observed transaction schema, coverage reports/database metadata, scope and project thresholds.

## Workflow
1. Map coverpoints/bins to requirements and meaningful boundary partitions. Define sampling event and distinguish attempted, accepted and completed operations.
2. Add selected crosses for meaningful interactions; estimate bin counts before creating them. Separate illegal behavior checking from coverage collection; illegal_bins alone is not a complete protocol checker.
3. Specify reset and warm-up gating. Avoid repeatedly counting stale data, unaccepted transfers or invalid transactions as architectural coverage.
4. Record code/functional/assertion coverage separately with exact denominator and exclusions. Normalize only compatible reports and preserve per-configuration results.
5. Classify holes as missing stimulus, missing observation, incorrect coverage model, DUT defect, unreachable under contract or unsupported configuration. Require evidence for unreachable claims.
6. Prefer a targeted test or constraint change tied to a gap over blind seed growth. Confirm the intended checker remains active when a bin is hit.
7. Track waiver owner, evidence and review condition; obtain required project approval before acceptance. Never remove bins or lower thresholds merely to meet a metric.

## Deliverables
Coverage model, requirement-to-bin map, gap analysis, closure actions and exclusion ledger.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Additional assets
- Use [closure.csv](assets/closure.csv) for the corresponding task ledger.
