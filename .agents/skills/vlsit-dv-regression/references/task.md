# Normalized result records
Use the bundled summarize_runs.py after normalizing vendor/project logs into JSON. It does not parse simulator output and cannot authenticate a PASS claim. The normalizer must inspect exit code, expected completion, required checker activity and unexpected errors before assigning PASS.

Input: a nonempty JSON list. Each row contains run_id, test, seed, configuration, status, command (argument array), tool_version, exit_code, log, reason. Use PASS, FAIL, NOT_RUN, UNSUPPORTED, INCONCLUSIVE or N/A. PASS requires exit_code 0 and log; other statuses require a reason. Retain TIMEOUT/BUILD_ERROR/INFRA_ERROR in reason while using FAIL or INCONCLUSIVE as appropriate.

Invoke: python3 scripts/summarize_runs.py runs.json --out summary.json
Relative script paths are relative to this skill directory; pass project input/output paths explicitly. The helper refuses to overwrite output files and summarizes recorded claims only.
