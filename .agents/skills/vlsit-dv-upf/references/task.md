# Power-intent review and power-aware verification

## 1. Establish the power architecture
Pin the IEEE 1801/UPF language edition, simulator/version and supported feature subset. Collect RTL/netlist revision, UPF files and load order, hierarchy scopes, technology mappings, power-controller specification, supply model and integration constraints. Do not infer the project edition from the latest published standard.

Inventory power domains, primary/retention/always-on supplies, switches, legal power states, voltage states, control signals, clocks and reset domains. Distinguish architectural power intent from implementation refinement. A file parsing successfully does not prove the intended elements are bound to the intended domain.

## 2. Review resolved intent
Inspect elaboration reports for actual element membership, supply connectivity, effective strategies and unresolved/empty selections. Check hierarchy changes, wildcard matches, reused IP scope and top-level integration overrides. Report unintended overlaps or omissions rather than silently broadening selectors.

Record isolation direction, clamp value, location, control polarity and supplying domain. Review level-shifting requirements across specified voltage states and library mapping where implementation is in scope. RTL power-aware simulation cannot establish physical cell placement or analog voltage safety.

For retention, identify retained elements, retention supply, save/restore controls, legal timing and non-retained state. Determine whether resets override restored values and whether memory retention is modeled. Do not treat every register as retained merely because recovery tests pass.

## 3. Define the legal state/transition graph
Build a table of domain/supply states and a separate table of allowed transitions. Record dependencies on parent domains, always-on control, clocks, reset and firmware handshakes. Include steady-state dwell and transition entry/exit observations.

Derive ordering from the design contract. Typical shutdown/wakeup involves quiescence, save, isolation, supply change, clock/reset and restore, but there is no universal ordering suitable for every architecture. Write a partial order with named events and permitted intervals; preserve unspecified relationships as open questions.

## 4. Check isolation
Exercise source-off/destination-on paths and each relevant control polarity. Confirm the live receiver observes the specified clamp while the source can be corrupted. Test boundary transitions, isolation release and control availability. Avoid checking only that an enable toggled; inspect the protected interface behavior.

Record intentionally unisolated crossings with rationale. A blanket X mask at the scoreboard or receiver hides isolation failures. Apply expected-corruption rules only to the affected domain/state and maintain checks at architectural live boundaries.

## 5. Check retention and recovery
Write distinct non-reset data before shutdown, save under legal conditions, remove main power while maintaining the required retention supply, then restore and observe architectural state. Check retained and non-retained state separately. Include repeated cycles, reset interaction and an interrupted/illegal sequence only if its expected handling is specified.

For retention failure, distinguish missing save, missing restore, dead retention supply, incorrect element selection and reset overwriting restored data. A passing test with reset-value data is weak retention evidence.

## 6. Integrate traffic and checkers
Define what happens to in-flight requests: drain, reject, cancel, retry or retain. Update scoreboard, RAL mirror and coverage models according to observed transitions. Keep always-on/wakeup agents active as needed while preventing illegal stimulus into unavailable interfaces.

Check wake-up causes, interrupt handling and power-controller acknowledgements. For DVFS or frequency changes, specify supported state transitions and clock stability assumptions; digital simulation alone does not validate analog ramp behavior.

## 7. Coverage and negative sensitivity
Cover required states, legal transitions, transition pairs, domain interactions, retention groups and traffic/reset combinations. Sample completed observed transitions rather than requested commands. Record checker activity alongside state/transition coverage.

Use controlled faults such as wrong clamp, skipped save or premature release in isolated test variants to demonstrate detection, where modeling support permits. Do not ship faulted UPF as the production intent. Unexpected warnings, unsupported constructs and unresolved bindings remain visible even when functional traffic passes.

## 8. Acceptance evidence
Report static intent checks, elaboration/binding, dynamic corruption/isolation/retention behavior, coverage and implementation-level checks separately. If power-aware simulation support is missing, provide a static review and unexecuted test plan with NOT_RUN/UNSUPPORTED status. Ordinary RTL simulation cannot substitute for supply-aware semantics.
