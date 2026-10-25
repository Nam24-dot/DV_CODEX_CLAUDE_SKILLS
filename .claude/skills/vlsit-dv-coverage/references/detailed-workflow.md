# Coverage construction and closure

## Sampling contract
Define the event and object ownership for every covergroup. Architectural transfer coverage normally samples accepted or completed observed traffic; attempted/illegal traffic can have a separate model. Gate sampling during reset, invalid data or power states according to the specification.

Separate per-instance behavior from aggregate type coverage. Ensure repeated sampling of the same retained transaction does not inflate hits. Map bins to requirement IDs and explain partitions for values, transitions and concurrency.

## Bin and cross design
Estimate cross size before implementation. Cross risk-relevant partitions rather than every bit pattern. Distinguish ignored combinations, illegal combinations and unreachable combinations; each needs a different justification. Use checkers for forbidden behavior rather than relying solely on illegal_bins.

Include interactions such as reset with pending traffic, errors under backpressure, supported parameter extremes and power transitions. Do not add impossible combinations solely to appear comprehensive.

## Database provenance
Capture RTL/TB/spec revision, configuration, simulator/version, coverage model hash, run IDs and merge command. Reject or explicitly map incompatible models and elaborations. Keep per-configuration holes visible after any aggregate merge.

Preserve reported numerator, denominator, exclusions, weights and metric definition. Report code, functional, assertion and requirement coverage separately. Do not average percentages with different denominators without a justified metric.

## Hole investigation
| Suspected cause | Discriminating evidence | Action |
|---|---|---|
| Missing stimulus | Required partition never generated | Directed scenario or constraints |
| Rejected stimulus | Generated but never accepted | Driver/protocol/backpressure investigation |
| Missing observation | Transfer visible but no sample | Monitor/connectivity/sampling repair |
| Model error | Incorrect bin expression or gate | Fix model and invalidate affected database |
| DUT defect | Required behavior absent with valid trigger | Debug with first-failure evidence |
| Unreachable | Contract/proof excludes behavior | Reviewed exclusion with scope |
| Unsupported configuration | Feature absent by specification | Record applicability, do not fake execution |

## Closure experiment
Change one targeted stimulus/model condition, rerun a bounded case, and show the intended bin plus the corresponding checker activity. If the bin is hit with a disabled scoreboard, record observation only and retain the correctness gap.

Track waiver owner, rationale, source evidence, affected bins/configurations, approval and review/expiry condition. Reassess waivers after model/spec changes. A closure report includes remaining holes and denominators before and after approved exclusions, without silently improving the headline percentage.
