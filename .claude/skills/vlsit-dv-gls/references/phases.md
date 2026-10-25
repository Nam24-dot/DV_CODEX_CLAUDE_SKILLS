# Three-phase GLS methodology

Use the following project terminology. Both phase 2 and phase 3 are post-simulation; record the phase ID so results cannot be confused. These names describe this suite's workflow, not a universal simulator naming convention.

| Phase ID | Project name | Required design input | SDF | Main objective |
|---|---|---|---|---|
| PRE_SYNTH | Pre-simulation (after synthesis) | Synthesized gate-level netlist and matching cell/macro models | No | Establish functional behavior, initialization and testbench integration on the synthesized netlist |
| POST_PNR | Post-simulation (after place and route) | Post-place-and-route netlist and matching models | No | Check functional behavior and integration on the physically implemented netlist |
| POST_PNR_SDF | Post-simulation (after place and route + SDF) | Post-place-and-route netlist, matching models and matching extracted SDF | Yes | Check exercised behavior with annotated delays and required timing checks for the selected corners |

Power-aware operation and functional/scan modes are additional dimensions of each applicable phase, not alternative phase definitions. Record the actual delay model and timing-check options in all phases: no SDF does not necessarily mean zero delay because library models and simulator settings may introduce delays.

## Phase 1: PRE_SYNTH
1. Freeze synthesis output revision, top, synthesis configuration, cell-library/model identities, macro models and testbench revision.
2. Resolve generated/renamed hierarchy, scan/test controls if present, tie cells and unmodeled instances. Review RTL-specific binds/backdoors before reuse.
3. Run reset/initialization, boot or basic configuration, representative data traffic, clock-gating behavior where implemented, and checker-sensitivity scenarios selected by risk.
4. Check accepted/completed traffic, scoreboard activity and pending-work cleanup. Investigate uninitialized state, missing models and sampling assumptions before progressing to broader runs.
5. Deliver a functional baseline and unresolved issues. A functional pass here is neither formal equivalence evidence nor post-layout timing evidence.

## Phase 2: POST_PNR
1. Use the place-and-route output netlist, not the synthesis netlist relabeled as post-simulation. Record its source revision and the implementation changes relevant to simulation, including clock-tree, buffer and ECO changes where present.
2. Revalidate library/macro bindings, hierarchy, power/ground connections, test controls and clock/reset routing visible in the netlist. Rebuild rather than silently reusing the PRE_SYNTH executable.
3. Run a comparable baseline without SDF. Preserve test, configuration and stimulus identity to help localize differences from PRE_SYNTH while accounting for changed hierarchy or legal latency.
4. If behavior diverges, investigate implementation connectivity, ECOs, model binding, initialization and testbench assumptions. Do not attribute every failure to extracted timing when no extracted SDF is loaded.
5. Deliver the post-PNR functional baseline. Record no-SDF scope explicitly; do not infer post-layout timing closure from this phase.

## Phase 3: POST_PNR_SDF
1. Pair the exact post-PNR netlist revision with its extracted SDF and matching library models. Record extraction/PVT corner, min/typ/max selection, annotation root and simulation precision.
2. Audit annotation diagnostics and intended scope before interpreting the run: attempted/annotated/unmatched/rejected entries, conditional arcs and timing-check support.
3. Run required corner/mode scenarios with acceptance timing checks enabled according to the project policy. Preserve all suppressions and exclusions. Disabled-notifier or disabled-timing-check reruns are diagnostic variants, not replacements for the required timing run.
4. Inspect setup/hold, recovery/removal, pulse-width and other supported checks, tracing the earliest timing event and X propagation. Keep independent functional checking active under the specified sampling contract.
5. Compare with POST_PNR using matched inputs to distinguish annotation/timing effects from functional-netlist or testbench defects. A missing no-SDF baseline limits diagnosis; report it and continue the authorized analysis rather than forcing unrelated reruns.
6. Deliver separate results for every required corner and mode, plus annotation and violation evidence. Passing exercised scenarios is not exhaustive timing closure and does not replace STA.

## Phase transitions and evidence reuse
Each phase has its own build/run identity and outcome. Do not copy PASS from one phase to another or merge their coverage without an explicit compatibility policy. Changed netlist, SDF, libraries, ECO or testbench invalidates affected evidence and requires impact review.

Run the phase requested by the user with available inputs. Earlier phases are useful diagnostic baselines, not mandatory approval gates. Mark missing required artifacts/checks as NOT_RUN or UNSUPPORTED and report the affected scope. The phase matrix in the output template records all three phases without inventing execution.
