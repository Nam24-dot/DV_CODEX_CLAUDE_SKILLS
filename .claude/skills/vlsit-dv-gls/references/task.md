# Gate-level simulation workflow

## 1. Select the verification question
Use [the three-phase methodology](phases.md): PRE_SYNTH after synthesis without SDF; POST_PNR after place and route without SDF; POST_PNR_SDF after place and route with SDF. Power-aware operation and functional/scan mode are independent dimensions. A passing no-SDF run does not establish timing correctness; a passing GLS regression does not replace STA, equivalence checking, ATPG or CDC sign-off.

Choose a focused scenario set from project risk: boot/reset, representative traffic, clock gating/switching, scan-enable transitions when in scope, memory initialization, asynchronous interfaces and low-power entry/exit. Full RTL regression replay is not automatically the best use of GLS runtime.

## 2. Inventory and match artifacts
Collect netlist hash/revision, top hierarchy, generated-clock and reset map, standard-cell simulation models, IO/memory/macro models, SDF file, testbench revision, simulator/version and original build target. Confirm libraries correspond to the netlist cells and intended timing/power behavior. Do not substitute empty stubs for required macros without an explicit abstraction limit.

Check functional versus scan netlist, tie cells, power/ground connections, test-mode controls, black boxes and unresolved instances. Review optimized/renamed hierarchy before reusing RTL bind paths, backdoors or hierarchical forces. Preserve mapping files where available.

## 3. Bring up elaboration and reset
Compile the actual cell models, netlist and TB with compatible options. Resolve duplicate modules, missing primitives, timescale/timeunit/timeprecision mismatches and library selection before running timing experiments.

Establish clock/reset behavior using the project's intended sequencing. Identify state that is reset, software-initialized, loaded through memory files, retained or intentionally unknown. Blanket register forcing can hide real initialization defects; record narrowly scoped debug forces separately from acceptance runs.

## 4. Audit SDF annotation (POST_PNR_SDF)
Record SDF producer/version, design identity, process-voltage-temperature corner, interconnect/cell-delay content, annotation instance and selected min/typ/max values. A field selection is not by itself a complete PVT specification. Confirm simulator precision can represent relevant delays.

Capture annotator diagnostics and counts by supported category: attempted, annotated, unmatched, rejected and not applicable. Inspect instance names, escaped identifiers, conditional arcs, timing-check support and hierarchy stripping. No universal percentage threshold is prescribed; reconcile missing annotation with required scope and project policy.

Verify representative cell and interconnect arcs against the intended hierarchy/report. A log saying the SDF file opened is insufficient. If the tool cannot report a denominator, state that limitation and use additional scope checks rather than reporting 100% annotation.

## 5. Timing-check and X investigation
Classify setup/hold, recovery/removal, pulse-width and other model diagnostics by cell, pin, edge, timestamp and stimulus context. Trace the earliest timing violation or X source before later functional mismatches. Check whether the issue comes from DUT timing, unrealistic TB drive, reset release, unsupported annotation or model mismatch.

Notifier-driven X can be useful evidence. A diagnostic rerun with timing checks/notifiers disabled may localize the cause, but must be labeled diagnostic and cannot establish timing-clean acceptance. Never edit SDF values or globally suppress violations to obtain PASS.

## 6. Sampling and scenario execution
Review RTL-era sampling assumptions under propagation delay. Use the interface's intended sampling contract; do not add arbitrary sleeps until mismatches disappear. Keep independent end-to-end checks even if some RTL-internal assertions cannot bind to the optimized netlist.

Run the required corner/mode/scenario matrix with immutable inputs. Recheck activity, comparison counts, pending traffic and clean termination. Separate expected power corruption from unexpected X at live interfaces in power-aware GLS.

## 7. Evidence and handoff
Deliver compile/elaboration evidence, annotation ledger, scenario results, violation ledger, X-root-cause report and limitations. Link each exception to instance/path, corner, mode, technical rationale, owner and review condition. Keep STA/equivalence/DFT reports as separately sourced evidence if the project requires them.

## Diagnostic decision table
| Observation | Investigate first | Acceptance consequence |
|---|---|---|
| Most SDF instances unmatched | Annotation root, netlist/SDF pairing, hierarchy | Timing coverage unresolved |
| X immediately after reset release | Recovery/removal, unreset state, library notifier | Preserve first event; do not blanket force |
| Functional run passes, SDF run fails | Timing event and monitor sampling | Functional pass cannot close timing failure |
| Macro outputs remain X | Model, initialization, power pins, clock/reset | Missing valid model limits scope |
| Only disabled-notifier run passes | Original timing checks and waveform | Diagnostic result only |
| RTL backdoor no longer resolves | Netlist optimization/name mapping | Repair mapping or use observable access |
