# Reference Model and Matching Contract

## Oracle
List authoritative requirement IDs, accepted-input events and independent prediction algorithm. Identify manually calculated vectors used to check the model itself.

## Representation
Define bit widths, signedness, arithmetic overflow, endianness, byte masks, four-state behavior and response/error handling.

## Temporal behavior
State input/output event order on the same edge, latency guarantees, matching key, ID reuse, per-ID ordering, outstanding limits and reset epoch policy.

## Check outcomes
| Condition | Expected diagnosis | Required evidence |
|---|---|---|
| Payload corruption | Mismatch with expected/actual | Controlled sensitivity test |
| Unexpected response | No matching accepted request | Monitor/model transaction trace |
| Duplicate response | Duplicate or unexpected response | Matching history |
| Missing response | Contract deadline failure or test watchdog/pending failure | Pending state and specified bound |
| Reset with pending work | Contract-defined flush/retain/cancel | Reset and transaction trace |

## Completion
State accepted, predicted, compared, cancelled and pending counts. Explain the accounting equation for this protocol; do not assume one response per request for every design.
