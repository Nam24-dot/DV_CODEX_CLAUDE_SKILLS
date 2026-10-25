# VIP selection, integration and qualification

## 1. Capability and compatibility inventory
Identify protocol family/issue, endpoint role, feature subset and abstraction level for each VIP: transaction-level agent, pin-level BFM, memory model, protocol checker or PHY/link model. Determine what it drives, observes, checks and covers. Internal reusable agents require the same explicit contract as commercial VIP.

Record vendor/product/release/patch, simulator/version, SystemVerilog/UVM baseline, OS/architecture, required DPI/shared libraries and available licenses. Use the installed release's compatibility matrix and example filelists. Do not assume all native UVM VIP supports every simulator, encrypted-source format or UVM implementation.

Identify required unsupported features early. Distinguish a missing license from an unsupported feature and a broken integration. Keep proprietary paths/configuration local; publish portable variable names and version requirements instead of vendor payloads or credentials.

## 2. Instance roles and ownership
| DUT role | Typical VIP role | Ownership review |
|---|---|---|
| Request initiator/manager | Active responder/subordinate | VIP drives responses/backpressure; DUT drives requests |
| Request target/subordinate | Active initiator/manager | VIP drives requests; DUT drives responses |
| Existing driven link | Passive monitor/checker | No second active driver; checker and coverage settings reviewed separately |
| Bidirectional/link-training interface | Role from protocol/link model | Resolve direction, training, reset and electrical/model responsibilities |

Role and active/passive are separate configuration axes. A passive agent may still check and cover, depending on the product; inspect effective settings rather than assuming passive means checking disabled. Clock/reset ownership must also be explicit. Detect accidental competing drivers and disconnected receivers before debugging data mismatches.

## 3. Build bring-up
Use the existing project build system. Preserve vendor package/include/library order and supported compile/runtime options. Avoid compiling two incompatible UVM implementations or mixing precompiled VIP libraries with a different ABI/tool configuration. For DPI, inspect bitness, search paths, dependent libraries and exported symbols using documented tooling.

Run a shipped minimal example on the selected simulator when possible to distinguish installation/license problems from DUT wiring. Record this separately from integration evidence. If the example is unavailable or execution is blocked, continue configuration/source review and name the missing check.

## 4. Project wrapper and configuration
Keep product-specific types, configuration construction and callbacks behind a narrow wrapper where practical. Do not create a fake universal API that conceals different protocol semantics. Maintain an API mapping with actual class/field/port names and documentation references from the installed release.

Configure each instance with typed objects and precise config_db scope. Set role, width, address map, endian convention, supported features, outstanding limits, reset behavior, timeout policy and checker/coverage enables according to the DUT contract. Review defaults explicitly, especially automatic traffic, response generation, protocol options and severity control.

Check topology and interface/modport types, parameterization, pin directions, clocking and sample/drive skew. Connect sequencers only where active traffic is intended. Some products use static interface/BFM binding rather than a standard virtual interface; use documented integration paths.

## 5. Sequence and response integration
Adapt project scenarios to supported vendor sequences or transaction APIs. Confirm which fields are randomized and which require explicit configuration. Preserve request/response identity and handle responses using the actual VIP mechanism. Vendor default sequences must not silently run concurrently with project-controlled sequences.

For responder VIP, define legal backpressure, response latency, errors and storage behavior. A default memory responder is not automatically an independent model of a complex DUT. Bound waits according to specified guarantees; distinguish infrastructure watchdogs from protocol deadlines.

## 6. Monitor conversion and architectural checking
Consume observed accepted/completed transactions, not only issued sequence items. Determine whether each callback/analysis port reports request start, acceptance, response completion, beat or assembled packet. Convert at the correct semantic event and avoid counting two streams as duplicate architectural operations.

Preserve ordering domain, ID, beat/last information, address, payload, byte enables, response status, timestamp and epoch. Document any lossy conversion and its effect on checking. Copy/clone retained objects according to vendor ownership rules; some callbacks reuse mutable transaction handles.

Connect normalized streams to independent end-to-end scoreboards, functional coverage and RAL prediction as applicable. A VIP protocol checker establishes its enabled protocol checks, not the DUT's algorithmic correctness. Choose one RAL prediction strategy per path and prevent duplicate prediction.

## 7. Reset and power lifecycle
Specify partial-transaction handling, response cancellation, internal VIP queues, sequencer recovery and post-reset initialization. Determine how the VIP observes or is notified of reset. Never assume clearing the project scoreboard clears the VIP's outstanding state.

For power-aware tests, define which instances remain always-on, which become passive/quiescent, and when checking legitimately gates or resumes. Preserve checks at live receiver boundaries. Restore checking after wake-up and demonstrate new traffic; a permanently disabled checker is not a recovery pass.

## 8. Checker and coverage ownership
Inventory enabled protocol checks, severity overrides, waivers, unsupported checks and replacement assertions. Record product rule IDs and the exact scope/reason for any suppression. Negative tests should expect a specific diagnostic without globally demoting errors.

Map VIP coverage to requirement intent and retain the vendor denominator/model version. Add DUT-specific coverage for architectural interactions not represented by VIP bins. Avoid double counting duplicated monitors/collectors. Merge only compatible VIP releases/configurations with the tool's supported policy.

## 9. Integration qualification
| Scenario | Evidence |
|---|---|
| Installation example | Correct package/tool/license setup; separate from DUT result |
| Passive observation | Nonzero monitor/checker activity without signal driving |
| Directed smoke | Known payload accepted/completed and independently compared |
| Backpressure | Correct stall handling and stable observed fields |
| Multiple instances/outstanding | Correct routing, ID/order handling and no configuration cross-talk |
| Reset with pending work | Expected cancellations/drain and successful new-epoch traffic |
| Error response/injection | Exact expected detector and subsequent recovery |
| Checker sensitivity | Controlled violation triggers an enabled named check |
| Test completion | VIP/project queues accounted for, watchdog inactive and objections released |

Freeze the product release, effective configuration and check settings with each result. Report build/elaboration, vendor-example execution and actual DUT integration separately. Supply exact reproduction commands and unresolved feature gaps.
