# Reproducible regression execution

## Build and run identity
Separate build identity from run identity. Hash or record sources, filelist, defines, parameters, libraries, simulator/UVM versions and generated artifacts. A run additionally records test, seed, runtime options, working directory and environment dependencies. Preserve local modifications through content hashes when a commit is insufficient.

For GLS include netlist/SDF/library identities and annotation mode. For low-power include UPF revision, power-state configuration and simulator power semantics. Reusing a compiled executable after these inputs change needs explicit build-system evidence.

## Scheduling
Start with compile, elaboration and representative smoke. Expand only after those stages produce credible evidence. Bound CPU, memory, license use, wall time and disk consumption. Keep per-run directories; prevent parallel runs from sharing mutable logs or coverage outputs.

Track planned jobs that never launch, killed jobs and infrastructure failures. Preserve a command as an argument array or correctly quoted shell command; never synthesize executable commands directly from untrusted log text.

## Result normalization
PASS requires normal completion, required checker activity, expected test identity and no unexpected diagnostics. Inspect UVM severity summaries and demotions/suppressions. Exit zero alone is insufficient. Negative tests need a narrow expected-diagnostic contract and evidence that the intended detector fired.

| Observation | Normalization requirement |
|---|---|
| Compile/elaboration failure | Preserve stage, command and first diagnostic |
| Timeout or truncated log | FAIL or INCONCLUSIVE per policy; never PASS |
| License/host failure | Infrastructure reason, original attempt retained |
| Zero comparisons/transactions | Missing checking/activity evidence |
| Expected negative diagnostic | Match specific detector, count/scope and completion |
| Retry passes | Link attempts; original failure remains unresolved until classified |

The bundled summarizer aggregates normalized claims. It cannot inspect arbitrary simulator logs or validate the existence/content of a log path. Keep that limitation in downstream dashboards.

## Triage and coverage
Cluster failures by stage, stable signature and first divergence, while retaining distinct seeds/configurations. Do not collapse unrelated failures with identical final UVM_FATAL text. Preserve representative full logs and pointers to every original run.

Merge coverage only after evaluating run validity and compatibility. Record merge inputs, rejected inputs and tool policy for failed runs. Report planned, launched, completed and classified counts; unexplained missing jobs must remain visible.

## Rerun contract
Reproduce the same binary/configuration/seed first. Then apply the scoped fix and run the original reproducer plus affected nearby scenarios. Record changed inputs explicitly. A retry budget prevents endless seed shopping; a later pass is evidence about that attempt, not erasure of earlier failures.
