# Temporal properties and formal harness review

## Property worksheet
Record requirement, owner of obligation, clock, reset semantics, antecedent, allowed response interval, cancellation and unknown policy. Resolve whether the response can occur in the trigger cycle or only later. Translate a timing diagram into sampled cycles before choosing implication operators.

Guard history-dependent expressions after startup/reset when prior samples are not meaningful. A disable condition can abort obligations; check reset behavior separately when it is itself a requirement. Do not assume asynchronous disable semantics implement a synchronous reset requirement.

## Assertions, assumptions and covers
Assertions describe required DUT behavior. Assumptions constrain legitimate environment behavior. Covers demonstrate meaningful reachability, including antecedent activation, reset release, traffic acceptance and corner sequences. Label a property differently when reusing a block interface as environment versus DUT.

Avoid assuming a response, ordering guarantee or output stability that the DUT must establish. Review fairness explicitly: an eventually-ready assumption can make liveness provable but may be unjustified in the system. Keep bounded response and unbounded eventual response distinct.

## Harness bring-up
Inventory clocks, initial state, reset sequence, parameters, input constraints, black boxes, memories and abstractions. Confirm tool support for the chosen language constructs and multi-clock modeling. A syntax-accepted harness may still overconstrain reachable behavior.

Run reachability covers before relying on proofs. Investigate contradictory constraints, permanently asserted reset and disabled properties. Use assumption review and tool-supported consistency/vacuity analysis; cover success alone does not establish complete assumption adequacy.

## Result classification
| Result | What to preserve |
|---|---|
| Counterexample | Trace, shortest meaningful divergence, property/harness revision |
| Bounded no counterexample | Bound, initialization and assumptions; no universal claim |
| Unbounded proof | Tool proof result, engine/abstraction scope and assumptions |
| Timeout/unknown | INCONCLUSIVE, explored depth/progress and resource limit |
| Unreachable cover | Tool result and constraints; distinguish bounded failure to reach |
| Unsupported property | Exact unsupported construct and alternate check if available |

## Debug and sensitivity
For each counterexample classify DUT defect, incorrect property, bad assumption or modeling artifact. Reproduce relevant behavior in simulation where useful, without treating simulation agreement as proof.

Exercise legal traces and controlled violations. For a stall-stability property, include a real stalled transfer and a payload change under stall; simply proving an implication without any stall is weak evidence. Keep checker activation separate from functional coverage.

When a proof is decomposed, record assumptions and guarantees at cut points and how they are discharged. Do not hide unresolved dependencies behind a collection of individually passing proofs. CDC/RDC and analog metastability require their own analysis scope.
