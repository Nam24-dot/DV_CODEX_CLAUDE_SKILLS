# Design Verification Rules — version 1.0

This is an independently authored project policy, not an IEEE standard or an official VLSIT rule. Read the complete document before executing the skill. User requirements and repository policy take precedence; surface technical conflicts rather than silently redefining expected behavior.

## Scope and evidence
DV-001 MUST record DUT top, source/spec revisions, configurations, interfaces, clock/reset domains, and verification boundaries. If a specification is absent, label RTL-derived behavior as an inferred baseline, not independent correctness evidence.
DV-002 MUST give requirements stable IDs and map each to stimulus, an independent checker/property, coverage, and evidence. A test name alone is not a correctness check.
DV-003 MUST preserve existing changes and keep verification changes separate from DUT fixes. Do not change RTL, golden values, thresholds, assertions, or exclusions solely to obtain a pass.
DV-004 MUST record simulator/formal tool version, UVM implementation/version, compile options, filelist, defines, parameters, seed, command, exit code and log path for each executed run. Do not assume a commercial license or language feature exists.
DV-005 MUST classify each check as PASS, FAIL, NOT_RUN, UNSUPPORTED, INCONCLUSIVE or N/A. PASS needs inspected evidence within explicit scope. N/A needs a technical applicability reason; absent tools mean NOT_RUN or UNSUPPORTED. A timeout is never PASS.

## Testbench correctness
DV-006 MUST derive predictions from the specified contract and accepted input transactions. Do not copy DUT output into expected data or replicate its implementation as the only oracle.
DV-007 MUST define drive/sample timing, timeunit/timeprecision, handshake acceptance and reset priority. Prevent testbench/DUT scheduling races using the project's clocking/sampling convention; do not repair races with arbitrary delays.
DV-008 MUST specify reset handling for monitors, sequences, scoreboards, coverage and RAL. State which transactions are flushed, retained, cancelled or replayed; distinguish reset epochs if needed.
DV-009 MUST bound sequence waits and test completion. Require stimulus completion, monitor drain and scoreboard empty/pending checks. Ending objections is not evidence that all work completed.
DV-010 MUST prevent mutable transaction aliasing at analysis subscribers; use ownership or copies/clones where objects may change after publication. Preserve IDs, byte enables, errors and timestamps needed by consumers.
DV-011 MUST check randomize() results and label protocol-valid traffic separately from deliberate violations. Constraints must not remove required corner cases or impose unjustified DUT assumptions.
DV-012 MUST define four-state checking and unknown policy. Do not silently convert X/Z to zero, mask comparison failures, or disable checkers to pass a test.

## Assertions, coverage and proof
DV-013 MUST state assertion clock, reset disable semantics, sampled timing and any history-valid guard. Check activation/vacuity; prove assumptions are legitimate environment constraints, not desired DUT behavior assumed true.
DV-014 MUST distinguish bounded checks, unbounded proofs, covers, unreachable claims, abstractions and black boxes. Report depth, assumptions, tool result and unresolved properties. Simulation is not formal proof; lint is not simulation.
DV-015 MUST sample functional coverage from observed accepted behavior at the intended semantic event. Distinguish attempted stimulus, observed behavior and checker success. Avoid impractical cross-product growth.
DV-016 MUST retain coverage denominators, scope, configuration and exclusions. Do not merge incompatible builds or silently drop unreachable bins. Every waiver needs rationale, owner, evidence and expiry/review condition.
DV-017 MUST separate code, functional, assertion and requirement coverage. High coverage is not a substitute for correct checkers or a proof of absence of bugs.

## Delivery and sign-off
DV-018 MUST retain failed seeds and first-failure artifacts. A later rerun pass does not erase an earlier failure; classify flakes and fix infrastructure/testbench/RTL causes with evidence.
DV-019 MUST classify generated outputs as GENERATED_UNVERIFIED until relevant checks execute. Use VERIFIED_IN_SCOPE only for the named checks/configurations; use BLOCKED or DELIVERED_WITH_LIMITS for missing required evidence. Human project sign-off is a separate decision.
DV-020 MUST identify blockers and unresolved specification choices explicitly. Continue independent authorized work. Ask only for decisions that change behavior/scope, destructive actions, or approvals actually required by project policy; reuse existing authorization.

## Rule matrix
Record one row per applicable rule and scope: rule_id, scope, status, evidence, reason. Expand compound rules into subchecks when needed. Read these rules rather than treating an automatically generated matrix as a compliance proof. Do not omit failing rows.
