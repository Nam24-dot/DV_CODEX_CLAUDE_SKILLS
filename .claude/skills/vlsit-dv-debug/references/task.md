# Failure report
Include symptom, first-failure timestamp/cycle, expected/actual values, requirement, run identity, reproduction status, hypotheses, evidence, root cause confidence, fix scope and checks performed.

Log-only evidence rarely proves a DUT bug. A scoreboard mismatch may be stale expected state, sampling race, aliasing, reset precedence or real data corruption. A formal counterexample may expose invalid assumptions or a property error. Distinguish each with a discriminating experiment.

For nondeterminism repeat the exact build/seed and examine race sources and unseeded external randomness. A successful rerun alone is not a resolution.
