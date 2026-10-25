# Reference-model and matching design

## Define the oracle boundary
Write the accepted-input to expected-output transformation independently from DUT implementation. Specify arithmetic width, signedness, overflow, rounding, byte order, masks, errors and unknown-value handling. Use hand-calculated vectors or a separately justified model for model self-tests.

Choose the observation event per interface. A predicted response should be created only when the contract makes the request effective. For retries or rejected requests, record attempted traffic separately. Internal DUT state may aid debug but must not become the only expected-value source.

## Select a matching structure
| Contract | Candidate structure | Additional obligation |
|---|---|---|
| Globally ordered | FIFO queue | Document simultaneous enqueue/dequeue precedence |
| Ordered within each ID | Map of per-ID queues | Include ordering domain and reset epoch |
| Unique tag until completion | Tag-to-expected map | Detect premature tag reuse |
| Multi-beat response | Per-request assembly state | Beat count, last marker, partial masks |
| Split/merged output | Explicit transformation model | Conservation/accounting across boundaries |

An ID-only single-entry map is insufficient when multiple requests with that ID are legal. Matching by payload can hide duplicate or reordered data; use protocol identity and ordering semantics.

## Event scheduling
Avoid dependence on arbitrary arrival order of two analysis callbacks. Queue sampled events with cycle/time and process same-edge inputs/outputs according to the architecture. For zero-latency bypass, state whether a same-cycle accepted input can satisfy the output.

Analysis write functions cannot perform blocking waits. Use nonblocking enqueue plus processing tasks where required. Bound storage and report overflow as a testbench error, not silent data loss.

## Reset and power epochs
For each reset/power transition classify pending items as retained, completed before transition, cancelled or replayed. Flush only the classes allowed by the specification. Tag new traffic with an epoch and reject late old-epoch responses when the protocol does not permit them.

Distinguish expected corruption in an off domain from forbidden corruption at an isolated live receiver. Apply unknown-value policy per field/state; do not convert X/Z to two-state data before comparison.

## Sensitivity and end conditions
Exercise correct vectors, wrong payload, missing response, duplicate response, wrong ID/order and reset with pending traffic. Demonstrate the exact expected detector. A missing-response deadline needs a specified bound; otherwise use test-end accounting and a separate watchdog.

At completion report created, compared, cancelled and pending expectations, with a conservation equation appropriate to the model. Retain first mismatch context, expected/observed values, ID/epoch, requirement and nearest transactions. A zero-error report with zero comparisons is insufficient evidence.
