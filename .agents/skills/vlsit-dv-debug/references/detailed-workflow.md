# Failure localization and discriminating experiments

## Preserve the failing context
Capture source/build identity, test/configuration, seed, tool versions, exact command, first failure, waveform window and checker state. Identify build, elaboration, initialization, stimulus, checking, drain or infrastructure as the failing stage.

If only a log is available, distinguish observations from hypotheses. Request the minimum additional artifact that separates likely causes; do not claim a confirmed RTL defect from a mismatch message alone.

## Classify before editing
| Symptom | Candidate causes | Useful experiment |
|---|---|---|
| Wrong payload | DUT, byte order, stale model, aliasing | Trace accepted input through model to observed response |
| Missing response | Dropped request, stall, reset cancellation | Compare requested/accepted/completed counts and epochs |
| Duplicate response | Monitor double-sampling, DUT replay | Inspect physical handshake and publication counts |
| Hang | Objection, blocked wait, response queue, dead clock | Dump outstanding work and waiting components |
| Same-seed nondeterminism | Scheduling race, external RNG, changed build | Repeat immutable inputs and compare first divergence |
| X at gate level | Uninitialized state, notifier, missing model, power corruption | Find earliest X and timing/power event |
| Formal counterexample | DUT, property, assumptions, abstraction | Inspect shortest meaningful trace and obligation owner |

Use binary search in time or hierarchy only when it preserves event causality. Follow the earliest divergence rather than cascaded scoreboard errors.

## Hypothesis ledger
For each hypothesis record supporting evidence, contradictory evidence, a discriminating experiment and confidence. Change one variable at a time where feasible. Preserve diagnostic variants separately from acceptance runs.

Disabling an assertion, timing check or scoreboard can localize a cause but cannot become the passing configuration without a justified project decision. Likewise a forced initialization or fixed delay can hide reset/race issues.

## Minimize and repair
Reduce transaction count, seed scenario or hierarchy while retaining the failure trigger. Preserve protocol legality unless the test intentionally checks invalid behavior. Avoid replacing the independent oracle with DUT output.

Implement fixes only within the requested scope. A testbench repair should not silently change the design contract. For a spec ambiguity, isolate the affected expectation and continue independent checks.

## Validation and handoff
Keep a pre-fix failing reproducer, the scoped change, post-fix run and nearby regression. Check that the intended detector remains active after repair. If execution is unavailable, label the patch unverified and supply exact reproduction steps.

Report root cause separately from contributing conditions, affected configurations, residual uncertainty and prevention test. A passing rerun alone does not explain a flaky failure.
