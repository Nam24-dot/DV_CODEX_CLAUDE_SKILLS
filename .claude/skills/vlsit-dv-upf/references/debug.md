# Low-power debugging worksheet

| Symptom | Inspect | Discriminating check |
|---|---|---|
| No corruption after power-off | Resolved domain, supply state, simulator power mode | Observe a known non-retained internal element and effective supply |
| X reaches live receiver | Isolation strategy, clamp, supply and timing | Compare source corruption with receiver boundary before/after control |
| Retention restores reset value | Saved data pattern, save/restore, reset ordering | Use unique pre-off values and trace each relevant event |
| Wake-up deadlock | Always-on controls, clocks, reset and acknowledgement dependencies | Trace transition partial order and first unmet dependency |
| Registers disagree after wake-up | Retained set, hardware reset and RAL mirror policy | Frontdoor reads plus actual reset/power event history |
| RTL passes, power-aware fails | Supply/intent binding or real power-state defect | Reproduce identical traffic with explicit state trace |

Preserve the first incorrect supply/control/data event, not only the final scoreboard mismatch. Keep static-report, dynamic-simulation and physical-implementation findings separate. Any debug suppression must name its scope and be excluded from acceptance evidence.

## Version and source guidance
The [IEEE 1801 project and standards page](https://standards.ieee.org/ieee/1801/11890/) identifies the power-intent standard and related editions. Use the edition selected by the project and the simulator's documented support, not an unqualified 'UPF compliant' claim. Retrieve syntax from the licensed/public standard or installed tool help before writing version-sensitive commands. Do not invent vendor-independent supply-control APIs.
