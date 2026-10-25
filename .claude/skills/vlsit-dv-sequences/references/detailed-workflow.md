# Directed and constrained-random stimulus design

## Scenario contract
For each sequence specify requirement IDs, preconditions, legal ranges, configurable knobs, completion event and expected detector for negative traffic. Distinguish requested, accepted and completed operations. A sequence that generates a corner value has not demonstrated that the DUT accepted it.

Start with composable single-purpose sequences: boundary values, sustained stream, stalls, reset interruption, errors and recovery. Use virtual sequences only for actual coordination among interfaces. Keep timing ownership clear when a reset/power sequence runs concurrently with data traffic.

## Constraint review
Check sized literals, signedness, arithmetic overflow and relationships among length, address, size and byte masks. Verify hard constraints do not make a scenario unreachable. Treat distribution weights as stimulus choices, not evidence of coverage. Review solve-before only where its distribution effect is intended.

Check every randomize return and preserve the failing constraint context. Do not keep stale field values after failure. Prefer explicit legal partitions to repeated retries that hide inconsistency. Keep inline constraints compatible with base constraints; define how optional constraints are enabled or disabled.

## Scheduling and responses
Define request acceptance, outstanding limit, response matching and ID reuse. Collect responses even when requests are pipelined; unconsumed response queues can overflow or stall tests. If using locks/grabs or priority arbitration, bound ownership and release it on all termination paths.

Record simulator seed and any external RNG seeds. Use the project RNG methodology; adding a random object can change streams even with the same top-level seed. A failing sequence should preserve its effective configuration and transaction trace for reproduction.

## Reset, power and invalid stimulus
Specify whether interruptions cancel, drain, retry or replay pending requests. Stop obsolete responses from satisfying later waits. Do not assume a sequence stop automatically cleans driver state.

Protocol-invalid injection may require a specialized driver mode because a compliant transaction driver cannot express electrical violations. Scope the injection to a named event and checker; restore normal behavior and show recovery. Whitelist only the expected diagnostic, not all UVM errors.

## Scenario validation matrix
| Scenario | Observation | Required check |
|---|---|---|
| Minimum/maximum transaction | Monitor fields and acceptance | Correct data/mask/length |
| Long stall | Valid/payload over stall interval | Stability and eventual handling under stated bounds |
| Outstanding saturation | Accepted minus completed count | Limit obeyed; no loss or duplicate |
| Reset interruption | Old/new epoch IDs | Cancellation policy and restart |
| Directed invalid event | Exact detector activation | Expected diagnostic and recovery |

Report which required partitions were actually reached, not only which constraints were written. Use targeted sequences for holes before increasing random seed count.
