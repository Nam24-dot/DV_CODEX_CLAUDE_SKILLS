---
name: vlsit-dv-ral
description: "Create, review or debug UVM RAL register models, adapters and predictors. Use for register maps, frontdoor/backdoor access, mirrors, reset values, access policies and register test planning."
---

# UVM Register Model

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.

## Inputs
Authoritative register specification, bus version, endianness, address units/stride, reset domains and existing RAL generation flow.

## Workflow
1. Validate offsets, sizes, alignment, access widths, field overlap, reset values/masks and access policies against the specification. Record reserved, volatile and hardware-updated fields.
2. Use the existing generator/source-of-truth where present. Build blocks/maps/fields with correct byte addressing and endianness; lock the model at the intended stage.
3. Implement reg2bus/bus2reg with byte-enable, response and status handling matching the observed protocol. Configure sequencer/adapter and supports_byte_enable/provides_responses according to actual behavior.
4. Choose a single prediction strategy for each access path. Avoid duplicate explicit predictor and automatic prediction updates, especially for read/write side effects.
5. Configure frontdoor and validated backdoor paths separately. Explain that model reset changes the model state; it does not drive hardware reset.
6. Handle W1C/W1S/read-clear, volatile fields, asynchronous hardware updates and reset domains deliberately. Exclude destructive generic tests only with specific rationale and add suitable directed checks.
7. Execute reset/read-write/mirror/side-effect tests as applicable, verify bus errors and partial accesses, and report model-versus-DUT mismatches without masking them.

## Deliverables
RAL source/configuration, adapter/predictor integration, register test matrix and validation report.

Start from [task output template](assets/output-template.md). Read its headings before writing the project artifact.

## Completion
Report changed artifacts, requirement/configuration scope, checks actually run, remaining blockers and delivery status. Never claim hardware verification from skill validation alone.

## Additional assets
- Use [register-review.csv](assets/register-review.csv) for the corresponding task ledger.
