# UVM Architecture Contract

## Source and tool baseline
Record DUT/TB/spec revisions, top, filelist, simulator/UVM version and supported configurations.

## Agents
| Interface instance | Clock/reset | Transaction type | Active/passive | Driver ownership | Monitor acceptance event |
|---|---|---|---|---|---|

## Connections
| Producer analysis port | Consumer export/imp/FIFO | Transaction ownership/copy policy | Purpose |
|---|---|---|---|

## Timing and lifecycle
Specify driver update edge/skew, monitor sampling edge/skew, reset priority, publication event, response collection, end-of-test drain, watchdog and pending-transaction checks.

## Configuration
Record config object type, virtual interface type/modport, config_db scope, factory overrides and required versus optional values.

## Smoke evidence
Record build, elaboration, traffic accepted/completed counts, scoreboard comparisons, assertion activation, coverage sampling, outstanding count, reset case and exact run/log identity. Leave unexecuted results NOT_RUN.
