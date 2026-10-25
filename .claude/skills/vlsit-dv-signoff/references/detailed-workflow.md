# Evidence reconciliation and readiness decisions

## Freeze review inputs
Record acceptance-criteria revision, DUT/TB/spec revisions, tool versions and supported configuration matrix. Index raw run logs, coverage databases, proof reports, issue records and waiver approvals. Missing authoritative criteria blocks acceptance, though a scoped readiness review can continue.

## Reconcile evidence dimensions
| Dimension | Questions to answer |
|---|---|
| Requirements | Is each obligation checked in every required configuration? |
| Regression | Are planned runs accounted for, with credible completion/checker activity? |
| Coverage | Are denominators, exclusions, merge compatibility and remaining holes visible? |
| Assertions/formal | Are activation, assumptions, proof bounds and inconclusive results recorded? |
| Testbench | Has checker sensitivity and reset/pending behavior been demonstrated? |
| GLS | Are required netlist/corner/mode runs and SDF annotation evidence current? |
| Low-power | Are power states/transitions, isolation, retention and recovery checked? |
| CDC/RDC | Are constraints, crossing reports and scoped waivers reviewed? |
| Defects | Are unresolved failures, flakes and accepted risks tracked? |

Scope specialist dimensions by actual project criteria. Do not invent a requirement that every block needs every analysis, and do not silently mark required but unrun work N/A.

## Freshness and compatibility
Follow provenance from each claim to the exact artifact/run. A green summary for an older netlist, UPF, parameter set or coverage model cannot close a new revision without a justified equivalence/impact argument. Check that the accepted waiver still matches current paths and modes.

Compare requirement, test, checker and coverage inventories. Flag orphan requirements, tests without checking, bins without requirements, and checks whose activity is absent. Explain whether a gap is missing evidence, a known defect or a deliberate scoped exclusion.

## Waiver and defect review
Require technical rationale, scope, owner, approver, evidence and expiry/review trigger. Keep a technical FAIL distinct from a risk accepted by the project. Do not count approved waivers as executed PASS checks. Reopened or flaky issues remain visible until their disposition is justified.

## Decision and output
Use READY_FOR_REVIEW only when the recorded criteria and evidence support a human review recommendation. NOT_READY means known unmet requirements; BLOCKED means missing criteria/inputs prevent the decision. Explain mixed cases rather than hiding them behind one status.

Provide a blocker table with requirement/configuration, missing evidence, concrete next action, owner and dependency. Keep artifact delivery status, technical check outcomes and human acceptance as separate fields. No automated report authorizes tapeout or replaces the designated sign-off authority.
