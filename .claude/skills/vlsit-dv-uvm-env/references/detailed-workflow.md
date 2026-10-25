# UVM construction and integration

## Architecture contract
Inventory interface instances, transaction types, sequencers, agents, scoreboards, coverage collectors and RAL predictors. Define which component owns clocks, resets and power controls. Keep passive agents passive: no driver construction or sequencer connection unless the configuration requires active stimulus.

Use project-supported factory macros and parameterized type registration. Match constructors to object/component roles. Keep package and interface compilation order explicit; avoid relying on incidental include order.

## Configuration and connectivity
Use typed configuration objects for per-agent settings. Resolve virtual-interface type, modport, parameterization and config_db path. Fail clearly on missing required configuration; a broad wildcard that happens to work with one agent can misconfigure multiple instances.

Inspect topology and port connections after elaboration. Demonstrate that a transfer observed on each physical interface reaches the intended subscribers exactly once. Record factory overrides and verify the instantiated type when behavior differs unexpectedly.

## Driver and monitor contracts
For each channel define drive edge/skew, sample edge/skew, acceptance, stalls and reset priority. A driver request can remain unaccepted for many cycles; the monitor must publish based on observed acceptance rather than sequence intent.

Pair each fetched request with the correct completion mechanism. Define whether item completion means request accepted or response completed; use a separate response path when required. Preserve sequence/transaction identifiers for responses. Bound waits using the project's timeout policy.

Allocate a new monitored transaction or clone at the ownership boundary. Verify do_copy/field automation includes every retained field. Do not publish a handle then mutate it while subscribers still retain it.

## Reset and lifecycle
Specify how reset aborts a partially driven request, waiting response, sequencer arbitration and monitor assembly. Ensure cancelled operations cannot later be matched to new-epoch traffic. Reset management should not leave a driver blocked on a request or a sequence waiting for a response that cannot arrive.

Use objections for the intended test lifecycle, then explicit drain conditions for outstanding work. A fixed drain delay does not prove queues are empty. At check/report phases report accepted/completed counts, pending transactions, checker activity and errors. Keep a separate bounded watchdog for deadlock diagnostics.

## Integration checks
| Stage | Minimum evidence |
|---|---|
| Compile | Ordered files, selected UVM API baseline, no unresolved symbols |
| Elaborate | Correct topology, interfaces, active/passive configuration |
| Smoke | Nonzero accepted traffic, expected comparisons, clean completion |
| Backpressure | Held payload, no duplicate publication, response accounting |
| Reset | Mid-traffic cancellation/recovery and clean new-epoch traffic |
| Multiple agents | Correct routing and per-instance configuration |
| Negative sensitivity | Intentional corruption detected by the expected checker |

Keep build, elaboration and simulation results separate. If no simulator is available, provide source and integration commands as unverified artifacts, not a working environment claim.
