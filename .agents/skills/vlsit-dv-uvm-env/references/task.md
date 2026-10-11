# UVM integration review
Check package/import order; interface before virtual-interface users; macros inclusion; parameterized factory registration; config_db scope and type consistency; passive agent without a driver; sequencer-driver connection only for active agents.

For clocking blocks explicitly set and explain skews relative to the protocol. Verify what a monitor samples at the edge and when the driver updates values. Never prescribe one skew as universally correct.

Every monitor transaction includes enough context for consumers: acceptance time/cycle, reset epoch, ID where present, payload, mask, response and protocol error information. If subscribers retain handles, copy or clone at the ownership boundary and verify field-copy implementation.

Test completion needs meaningful traffic/checker counts. A UVM test with zero errors and zero transactions is not adequate smoke evidence. A watchdog should report outstanding transactions before terminating.
