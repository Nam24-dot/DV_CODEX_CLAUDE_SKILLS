# VIP debug, upgrades and specialist modes

## Failure triage
| Symptom | Inspect | Discriminating experiment |
|---|---|---|
| Compile/package failure | Release, UVM baseline, include/library order, encrypted-source support | Reproduce documented example with the same tools |
| DPI load failure | ABI/architecture, dependencies, search paths, version match | Inspect loader diagnostic and supported shared-library selection |
| License checkout failure | Product feature/version and available license | Preserve license error as infrastructure evidence, not DUT failure |
| No observed transactions | Interface mapping, role, sampling and port connection | Trace one physical handshake into the expected monitor callback |
| Multiple drivers/X | Active/passive and direction ownership | Inspect per-signal owners and unintended default traffic |
| Hang after request | Responder mode, sequence completion, response collection, clock/reset | Account for request acceptance and every outstanding response |
| Unexpected checker errors | Protocol variant, widths, optional features, sampling | Compare first offending transfer to the installed rule definition |
| False scoreboard mismatches | Callback phase, field conversion, object reuse, epochs | Preserve raw VIP event plus normalized transaction |
| Zero coverage or clean report with no traffic | Enables, licensing, sampling, reset gating | Exercise a directed accepted transfer and inspect activity counts |
| Wake-up never checks again | Checker gating and VIP reset/reinit state | Observe enable restoration and controlled post-wake traffic |

Do not patch encrypted/proprietary VIP internals, globally suppress diagnostics or alter expected data merely to make a run green. When vendor support is needed, prepare a minimal reproducer and version/log summary; share externally only within the user's authorization and disclosure rules.

## Vendor or release migration
Compare APIs, default configuration, transaction schemas, timing semantics, checker IDs/severities and coverage definitions. Recompile with compatible dependencies. Run the same directed vectors and interruption scenarios on both configurations where available; compare accepted/completed traces and independent checker results, not only summary PASS counts.

Retain original failing seeds and version-specific known issues. Reassess waivers and coverage compatibility rather than copying them across releases. A wrapper reduces source coupling but does not guarantee behavioral equivalence.

## GLS, low-power and acceleration
For PRE_SYNTH, POST_PNR and POST_PNR_SDF, review binding, hierarchy, library-delay effects and supported VIP sampling under the actual clock contract. A VIP proven with RTL timing may need documented integration adjustments; arbitrary delays are not a justified repair.

For UPF, review power-state awareness and receiver-side checking; distinguish intentional corruption from forbidden leakage into live interfaces. Use documented controls for quiescence/reset instead of global X masks.

Simulation VIP is not automatically an emulation-ready transactor. Check synthesizable partition, host/target transport and vendor-supported acceleration product before proposing hardware-assisted execution. Record unsupported modes explicitly.
