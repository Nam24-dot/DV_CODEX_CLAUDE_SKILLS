# Clock- and reset-domain crossing review

## Scope and inputs
Collect RTL/netlist identity, top, operating modes, clocks/generated clocks, resets, clock mux/gating controls, test modes, CDC/RDC constraints and tool reports. Pin tool/version and analysis configuration. Distinguish constraint/setup review, structural analysis, protocol verification and waiver review.

Ordinary digital simulation does not model analog metastability or establish MTBF. A structural crossing report alone does not prove the transfer protocol preserves data. Keep CDC and RDC as separate analyses even when the tool shares setup information.

## Domain and constraint audit
Inventory source/destination clocks, periods, phase/frequency relationships and which modes can change those relationships. Do not classify clocks as synchronous merely because nominal frequencies match. Generated/gated/muxed clocks need explicit source and mode relationships.

Map reset source, polarity, assertion/release semantics, synchronizers and affected sequential elements. Include soft reset, watchdog reset and independently powered/reset domains. Check constraint coverage for unconstrained clocks/resets, ignored endpoints and black boxes before reviewing violation counts.

Mode constraints and constants can remove real crossings. Tie every case analysis, false path, stable signal and abstracted interface to a source and applicability scope. Preserve unconstrained-mode risks rather than silently constraining them away.

## Crossing classification
| Crossing | Review focus |
|---|---|
| Single-bit stable control | Synchronizer structure, source stability and destination use |
| Pulse/event | Pulse width, rate, handshake/toggle scheme and event loss |
| Multi-bit data | Coherency protocol; independent bit synchronizers are not a general solution |
| Handshake | Data stability window, acknowledgement, reset and throughput |
| Async FIFO | Pointer scheme, reset behavior, full/empty correctness and physical constraints |
| Reconvergent control | Relative latency, common source and downstream functional safety |
| Reset-domain path | Independently asserted/released resets, data/control effect on live receiver |

For Gray-coded transfers, review source transitions and implementation constraints; a source coding property alone does not establish destination coherency under arbitrary physical skew. For pulses, sample tests at phase/rate extremes and prove the assumed rate limit where relevant.

## RDC-specific reasoning
Inspect paths where asynchronous reset changes a source flop while the destination remains active, even if both use the same clock. Review reset assertion effects as well as synchronized release. Different reset names do not necessarily mean independent domains; shared names do not prove equivalent effective reset behavior.

Check reset reconvergence, partial reset, reset sequence dependencies and reset of synchronizer/protocol state. Verify that one side of a handshake or async FIFO can recover from the supported independent-reset cases without stale events or false full/empty indications.

## Evidence-driven triage
For each finding retain source/destination endpoints, clocks/resets, mode, tool rule, structural path, functional protocol and disposition. Classify real defect, constraint error, recognized safe structure, abstraction limitation or reviewed waiver. Fix setup errors and rerun before claiming a violation is gone.

Require technical reasoning for safe/waived crossings, including the assumptions that make them safe and their enforcement. Never waive by broad hierarchy wildcard solely to reduce counts. Record owner, approver and review condition; reassess after RTL/constraint changes.

## Dynamic/formal checks and handoff
Use simulation/formal to check data stability, event accounting, FIFO ordering, handshake recovery and supported reset/mode transitions. State tool assumptions and avoid claims that digital checks measure analog metastability resolution.

Report analysis coverage, unresolved constraints, crossing inventory, high-risk findings, waivers and protocol-check evidence separately. Coordinate with timing/physical-design owners for implementation constraints and reliability analysis; do not invent universal synchronizer depth or MTBF targets.

## Source boundary
[Siemens Questa RDC overview](https://www.siemens.com/en-gb/products/ic/questa-one/design-solutions/reset-domain-crossing/) describes RDC as a distinct analysis that can reuse CDC setup. Use the installed tool's rule/constraint documentation for exact syntax and classifications; this workflow does not require that vendor.
