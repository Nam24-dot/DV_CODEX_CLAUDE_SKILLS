# Requirement decomposition and scenario design

## Establish an authoritative baseline
Record document revision, section/table, RTL revision and resolved clarification for each requirement. Split statements containing independently testable obligations. Distinguish behavior guaranteed by the design from assumptions on its environment and implementation details that are not externally required.

When documents disagree, retain both sources and isolate affected scenarios. Do not silently treat RTL as the specification. Mark derived behavior as inferred and keep it out of independent correctness claims until resolved.

## Build scenario partitions
| Area | Partitions and interactions to consider |
|---|---|
| Capacity/arithmetic | Empty/one/full, wrap, saturation, signed limits, parameter extremes |
| Transfers | Accepted versus attempted, backpressure, concurrent input/output, response errors |
| Ordering | Same/different IDs, multiple outstanding, response reuse, cancellation |
| Reset | Assertion/release, pending work, stalled transfer, repeated reset, warm/cold reset |
| Registers | Partial writes, reserved fields, volatile updates, side effects, error responses |
| Power | Legal states/transitions, isolation, retention, wake-up and reset interactions |
| Clocks | Ratios, stopped/restarted clocks, source switches and supported modes |
| Performance | Latency endpoints, sustained throughput, arbitration fairness under assumptions |

Choose partitions from supported behavior; do not label illegal configurations as legal tests. Cross only interactions that carry a specific risk and state why. A large Cartesian product without checking intent is not a plan.

## Turn each scenario into a checkable obligation
Record preconditions, stimulus, observation event, expected behavior, checker, coverage, completion condition and evidence. Specify whether latency is measured in source clocks, destination clocks or elapsed time. State inclusive bounds and behavior under backpressure.

Example: for a depth-N FIFO, 'full plus push' is incomplete until overflow policy and simultaneous pop semantics are known. Record these as unresolved if absent. A rejected push must not enter the accepted-input reference queue; an attempted-operation coverage bin can still record the stimulus separately.

## Risk and technique selection
Prioritize impact, likelihood and observability. Directed tests establish key boundary behavior; constrained-random exercises combinations; assertions enforce temporal obligations; formal explores specified state spaces under documented constraints. Each technique has different evidence and limitations.

Include checker sensitivity tests and a small smoke subset. Define which requirements cannot be observed at the chosen boundary and whether instrumentation, an alternate proof, or an explicit scope limit resolves the issue.

## Change impact and completion
Preserve requirement IDs when wording changes without changing identity. Record superseded/retired requirements separately. Map each changed requirement to affected tests, reference logic, properties, bins and configurations. Never reuse old PASS evidence merely because a test name is unchanged.

A complete plan has no unclassified requirement: every item is planned with a checking mechanism, explicitly blocked, out of scope with reason, or technically inapplicable. Planning completeness does not mean implementation or execution completeness.
