# Routing and milestones
Plan-only requests stop after a reviewable plan. Debug requests begin from the failing run rather than rebuilding the environment. Existing UVM projects should be extended in place. A small non-UVM testbench is acceptable when the project does not use UVM and its scope supports it; explain that choice.

Milestones: specification inventory → traceable plan → observable/checkable TB → smoke → regression/coverage closure → acceptance recommendation. These are dependency relationships, not compulsory human approval gates.

Example: For a FIFO, planning resolves simultaneous push/pop, overflow policy, reset and flag timing before a scoreboard encodes those decisions. Unknown behavior remains an open question instead of an invented expected value.
