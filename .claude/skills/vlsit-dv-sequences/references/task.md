# Stimulus review
Randomization failure is a testbench failure, not permission to use stale fields. Avoid repeated randomize-until-success loops that conceal contradictory constraints. Check signed arithmetic and sized constants in range constraints.

A sequence item is a requested operation. A monitor transaction is evidence of actual bus acceptance; use the latter for checking and architectural coverage. Invalid protocol injections need an explicit low-level mechanism and a defined expected detector/response; do not corrupt every driver.

Concurrency must specify ordering freedom and outstanding limits. Bound response waits and distinguish expected timeouts from test hangs. During reset, explicitly stop, drain or restart sequences according to policy and collect obsolete responses safely.
