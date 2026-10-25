# Register semantics and RAL integration

## Source-of-truth audit
Use the project's register generator when present; distinguish generated code from editable sources. Check address units, stride, alignment, register/field width, overlap, reset value/mask, access policy and reserved bits. Preserve spec revision and generator configuration.

For every side-effect field record value before access, returned read data, post-access state, hardware update and collision priority. W1C plus a simultaneous hardware set needs an explicit specification; the policy name alone does not resolve priority.

## Maps and adapters
Review byte addressing versus word addressing, endianness, bus width and multi-beat register access. Use asymmetric patterns to detect swapped lanes. Confirm reg2bus/bus2reg propagate address, data, byte enables and response status. Set adapter response behavior to match the actual driver contract.

Attach the intended sequencer/adapter to each map. Confirm submap offsets and aliased addresses. A successful RAL API call is not proof that the correct physical interface was used; inspect observed bus transactions.

## Prediction and mirrors
Choose auto prediction or explicit monitor-driven prediction per path and avoid duplicate updates. Define how frontdoor, backdoor, hardware changes and reset affect desired and mirrored values. A mirror is a model state, not an independent read of hardware.

Predict only completed operations with the specified error policy. Volatile hardware updates may require special comparison/prediction handling; blanket compare-disable loses meaningful checking. Document which independent check covers excluded mirror comparisons.

## Directed test matrix
| Area | Required cases when applicable |
|---|---|
| Reset | Each reset kind/domain, reset mask, retained versus reset fields |
| Access | RO/RW/WO, reserved fields, illegal address, bus error |
| Side effects | W1C/W1S, read-clear, self-clear, concurrent hardware update |
| Width/lane | Byte enables, partial writes, endianness, bus-word boundary |
| Paths | Frontdoor/backdoor consistency and intentionally different semantics |
| Integration | Multiple maps, prediction source, external bus-master access |

## Backdoor and generic sequences
Validate HDL paths against elaboration, including arrays, generated instances and gate-level renaming. Backdoor writes may bypass bus side effects; never assume equivalence to frontdoor behavior. Do not use force/deposit as a substitute for checking functional accesses.

Exclude destructive or unsupported fields from generic bit-bash using the project's mechanisms, with rationale and behavior-specific replacement tests. RAL model reset does not drive DUT reset. After reset/power recovery, update model state only according to the observed architectural sequence.
