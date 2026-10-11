# Planning checklist
Columns: requirement_id, source, behavior, priority, configuration, stimulus, checker, coverage, acceptance, owner, status, evidence.

Boundary candidates: minimum/maximum values; zero/one/full capacity; simultaneous operations; saturation/wrap; invalid addresses; partial writes; timeout limits; ordering; reset assertion/release; reset while stalled; clock gating where specified.

Keep latency exact: define source event, destination event, clock and inclusive bounds. A throughput measurement is different from single-transfer latency. For multiple clocks specify the timebase or synchronization assumptions.

Do not automatically test unsupported configurations as legal modes. Mark illegal configuration checks separately. A protocol label such as AXI does not establish data width, ordering capability or all optional features.
