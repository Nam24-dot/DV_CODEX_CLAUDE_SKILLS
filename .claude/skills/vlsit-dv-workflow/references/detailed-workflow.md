# Integration decisions and handoffs

## Select the work boundary
For an existing project, inventory compile targets, filelists, simulator/library versions, agents, monitors, reference models, coverage databases and run conventions before proposing changes. Separate block, subsystem and SoC responsibilities. Record software/firmware dependencies and externally supplied VIP models.

Use the smallest workflow that answers the request. A failing seed starts with debug; a coverage hole starts with the existing checker and sampling contract; a new interface starts with its specification. A planning request does not authorize implementation.

## Route specialist work
| Trigger | Skill suffix | Required handoff |
|---|---|---|
| Missing or changed behavior | testplan | Atomic requirements, contradictions, configuration scope |
| Pin/transaction architecture | uvm-env | Timing, ownership, active/passive roles |
| Scenario generation | sequences | Legal constraints, reset cancellation, completion |
| Expected/actual matching | scoreboard | Acceptance, ordering, reference-model contract |
| Temporal property or proof | sva-formal | Clocks, assumptions, activation, proof scope |
| Coverage hole | coverage | Compatible database identity, denominators, checker activity |
| Register behavior | ral | Register source, access semantics, prediction strategy |
| Run orchestration | regression | Reproducible commands, budgets, run records |
| Failing evidence | debug | First failure and immutable reproduction inputs |
| Netlist/SDF/timing notifier | gls | Netlist, libraries, SDF, operating mode and corner |
| Power intent or power transition | upf | UPF revision, power-state and sequencing contract |
| Clock/reset crossing report | cdc-rdc | Domain constraints, crossing inventory, tool evidence |
| Bus compliance | protocol | Protocol issue, supported features, endpoint roles |
| Readiness decision | signoff | Required evidence, defects, waivers, approver |

Suffixes refer to `vlsit-dv-<suffix>`. Discover installed siblings by their actual names; do not assume that a textual route invokes another agent or tool. Load only needed references. If multiple skills apply, keep one shared requirement and evidence ledger.

## Resolve integration dependencies
Define the monitor acceptance event before implementing architectural coverage or reference-model input. Define reset/power epochs before enabling pending-transaction checks. Resolve model/map/address units before connecting RAL prediction. Establish clock and mode constraints before assessing CDC results. For power-aware GLS, combine UPF and GLS evidence rather than assuming success in either flow establishes the other.

Track each handoff as producer, consumer, artifact revision, unresolved decision and acceptance check. Avoid passing only prose such as 'done': a scoreboard handoff needs transaction schema, matching rules and sensitivity results.

## Reassess after changes
| Change | Evidence to reconsider |
|---|---|
| Spec/parameter/port | Requirement map, stimulus partitions, model, assertions |
| Monitor/sample timing | Scoreboard comparisons, coverage, RAL predictor |
| Netlist/library/SDF | GLS elaboration, annotation and selected scenarios |
| UPF/power controller | State transitions, isolation, retention, reset recovery |
| Clock/reset constraints | CDC/RDC crossing classifications and waivers |

Record artifact provenance rather than assuming a shared Git commit makes every generated artifact current. Re-run affected checks; justify retained evidence individually. Handoff includes blocked work and dependencies so a later session can resume without inventing decisions.
