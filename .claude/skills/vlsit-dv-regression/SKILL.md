---
name: vlsit-dv-regression
description: "Prepare and run reproducible simulation regressions with seed/configuration manifests and conservative result classification. Use for smoke suites, test matrices, CI integration or regression result aggregation."
---

# DV Regression

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Existing simulator commands/build system, test/configuration list, resource/time budget, expected completion criteria and available licenses.

## Workflow
1. Discover working project compile/elaborate/run commands and tool versions. Do not invent universal VCS, Xcelium, Questa or Verilator switches or assume equivalent UVM support.
2. Define run IDs from test, seed, configuration and build identity. Keep separate output directories and immutable source/config snapshots or hashes.
3. Compile and run a representative smoke first. Expand to planned tests/seeds within the supplied resource budget; limit concurrency to license/CPU/memory availability.
4. Capture command, cwd, environment dependencies, version, seed, exit status, elapsed time, full logs and coverage paths. Do not store credentials in manifests.
5. Classify build failures, simulation failures, timeouts, infrastructure errors, incomplete logs and expected negative outcomes separately. Inspect project completion/checker markers and UVM severity summaries; exit zero alone is insufficient.
6. Keep reruns linked to original failures. Group failures by evidence without deleting unique seeds; invoke dv-debug for diagnosis.
7. Merge compatible coverage only after run validation. Report planned/executed/passed/failed/not-run counts and all missing evidence.

## Deliverables
Run manifest, per-run logs, regression summary and reproducible failure commands.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Additional assets
- Use [runs.example.json](assets/runs.example.json) for the corresponding task ledger.

## Result helper
Read the normalized record schema in references/task.md, then run [summarize_runs.py](scripts/summarize_runs.py) on inspected project records. It validates metadata only.
