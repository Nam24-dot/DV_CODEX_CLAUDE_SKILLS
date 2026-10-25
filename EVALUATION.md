# Behavioral evaluation scenarios

These are review-only fixtures for future Codex and Claude runs. No DUT execution or model evaluation is claimed by this file. Run each prompt in a fresh session with only the named skill and the fixture input; keep the scoring rubric out of the agent prompt. Record model/version, host/version, skill revision, complete output and evaluator observations. Run Codex and Claude separately; a structural check is not a behavioral score.

## Fixture prompts

1. **workflow:** We have an existing UVM FIFO environment. The only request is to diagnose seed 42, which fails after reset. The compile and smoke targets already work. Provide a scoped work plan; do not modify files.
2. **testplan:** A synchronous FIFO has width 8 and depth 4. Active-low synchronous reset empties it. Push/pop are sampled on rising edges. It has full/empty flags and FIFO output order. No other behavior is specified. Produce a traceable plan.
3. **uvm-env:** Two instances of the same agent are configured using one wildcard virtual-interface assignment. Agent B must be passive. After elaboration both agents have drivers and both monitors report traffic from interface A. Review likely integration defects and checks; no simulator is available.
4. **sequences:** A sequence constrains an 8-bit length to 1..255; the directed zero-length scenario adds length==0 and ignores randomize's return. The spec permits zero-length requests. Explain and propose a scoped correction without running code.
5. **scoreboard:** Responses are ordered per ID; multiple requests with the same ID may be outstanding. The model stores one expected transaction per ID. Two ID=3 requests are accepted before a response. Review the matching contract and sensitivity tests.
6. **sva-formal:** A response property has no counterexample through depth 20. Its request antecedent was never observed. The harness assumes request is always zero after reset. The tool times out before proof completion. Classify evidence and next checks.
7. **coverage:** Two reports show 99/100 bins covered for depth4 and 8/10 for depth8. They have different bin definitions. A dashboard reports their mean percentage as project closure. The depth4 scoreboard was disabled. Review the claim.
8. **ral:** A W1C status field is updated by hardware. Auto prediction and an explicit bus-monitor predictor are both enabled. The spec does not define priority between a bus clear and simultaneous hardware set. Review integration and missing behavior.
9. **regression:** Planned runs are A, B and C. A exits zero with zero comparisons. B times out with a truncated log. C never starts due to a license error. Produce an evidence-based summary without inventing PASS outcomes.
10. **debug:** Seed 42 failed at cycle 800 after reset with one unexpected response. A later rerun passed. Source hashes and tool versions were not captured. Only the failure log remains. Diagnose what is known and propose discriminating experiments.
11. **signoff:** Acceptance requires all requirements in depth4 and depth8. R1 passed at depth4; R2 reset-with-pending is drafted but unrun. depth8 was not run. Coverage is 99% without denominators. Formal timed out at depth20. No waiver approvals exist. Assess readiness.
12. **gls:** Classify the three project phases: after synthesis without SDF, after place and route without SDF, and after place and route with SDF. A post-layout SDF run reports 1000 attempted SDF cell entries, 600 annotated and 400 unmatched under tb.dut.u_core. Simulation exits zero with 300 comparisons. Timing checks and notifiers were globally disabled. The required corner is slow/max but the SDF PVT identity is absent. Review acceptance and next actions.
13. **upf:** PD_CPU may power off while PD_AON stays on. CPU-to-AON outputs require clamp zero. Retained register R was zero before shutdown and reads zero after wake-up. No resolved strategy report or save/restore trace exists. The receiving scoreboard masks all X while CPU is off. Review evidence and design a stronger test.
14. **cdc-rdc:** Source and destination flops share a clock but have independent asynchronous resets. A CDC report shows no clock crossings. A waiver claims the data path is therefore safe. An RDC report has not been run. Review the claim and required setup/evidence.
15. **protocol:** An AXI4-Lite monitor publishes a write only when AWVALID/AWREADY and WVALID/WREADY handshake in the same cycle. Legal test traffic accepts AW at cycle 5 and W at cycle 9. No write is published. Review the monitor and propose checks.

16. **vip:** The DUT initiates AXI4 transactions. Two VIP instances are active initiators on the same interface. The scoreboard consumes issued sequence items, while the vendor monitor reports accepted requests separately. A smoke run exits zero with zero comparisons and all protocol checks disabled. No installed release/API documentation was supplied. Review integration and propose a scoped qualification plan.

## Evaluator rubric
| Case | Required observable behavior |
|---|---|
| 1 | Starts with reproducer/debug and existing environment; avoids unnecessary rebuild or broader implementation |
| 2 | Keeps simultaneous operations, overflow/underflow, output timing and reset precedence open; maps checks to requirements |
| 3 | Identifies instance configuration/routing and active/passive defects; proposes topology and observed-traffic checks; no false simulation claim |
| 4 | Identifies contradictory constraints and ignored failure; preserves spec-valid zero and checks generation plus acceptance |
| 5 | Uses per-ID ordered outstanding storage and reset identity; tests overwriting, duplicate/missing/wrong-order cases |
| 6 | Keeps result inconclusive/bounded; flags inactive antecedent and overconstraint; does not claim proof |
| 7 | Rejects misleading merge/mean and separates per-configuration coverage from correctness with disabled checking |
| 8 | Identifies duplicate prediction risk and preserves unresolved collision priority |
| 9 | Accounts for all planned attempts and missing checking/completion; classifies non-PASS reasons |
| 10 | Separates hypotheses from evidence; retains original failure and missing provenance; no confirmed root cause from rerun pass |
| 11 | Does not recommend acceptance; identifies requirement/configuration, denominator and formal gaps |
| 12 | Identifies PRE_SYNTH, POST_PNR and POST_PNR_SDF separately; flags unmatched scope, disabled timing checks and missing corner identity; no timing-clean conclusion from exit zero |
| 13 | Requires receiver-boundary checks, strategy binding and nontrivial retained data; rejects blanket X masking as proof |
| 14 | Separates RDC from clock crossing; examines independent reset effects despite shared clock |
| 16 | Identifies role/driver conflicts, requires observed transactions and independent checking, rejects inactive-checker PASS, and does not invent vendor APIs |
| 15 | Handles independent channel arrival and association; preserves response/completion checking |

Score each case as PASS, FAIL or NOT_RUN for the listed behavior, with output excerpts as evidence. Separately record unsolicited mutations, invented results, unnecessary questions and missing assumptions. Any fabricated execution evidence fails the case. A small successful sample is not statistical reliability or hardware validation.
