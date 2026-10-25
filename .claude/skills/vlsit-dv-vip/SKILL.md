---
name: vlsit-dv-vip
description: "Integrate, configure and debug vendor or internal Verification IP in an existing testbench. Use for VIP/UVC/BFM bring-up, compatibility, wrappers, monitor conversion and checker/coverage integration; not general protocol-rule authoring."
---

# Verification IP Integration

## Operating contract
Read [DV rules](references/DV_RULES.md) and [evidence contract](references/evidence.md) in full. Read [task reference](references/task.md) for this workflow. Use engineering English for technical artifacts and code; answer the user in their requested language.

Use paths and decisions already supplied by the user or unambiguously established in the current project. Ask only for missing inputs that change expected behavior or prevent the next step. Mark assumptions explicitly. Preserve user changes. Discover tools before running them; report unavailable checks honestly. Use the bundled assets as editable starting formats, never as completed verification evidence.



## Inputs
VIP vendor/product/release, installed integration manual and examples, protocol issue/features, simulator/UVM versions, license availability, DUT interfaces/roles, existing TB/build targets and integration objective. Use known project settings; isolate unresolved API or behavior decisions without blocking independent review.

## Workflow
1. Inventory existing VIPs and supported tool/library combinations before choosing replacements. Read the installed release's documentation; never invent vendor class names, configuration fields, ports or switches.
2. Establish endpoint role and active/passive behavior per instance. Define one driver owner for every driven signal, plus clock/reset/power ownership.
3. Reproduce a shipped example when available, then integrate a minimal instance using the project's build flow and compatible UVM/DPI libraries.
4. Implement a narrow project wrapper and typed configuration. Map actual pins/interfaces, sequencers, monitor streams, protocol checks and coverage explicitly.
5. Normalize observed VIP transactions into the project's schema while preserving IDs, masks, errors, ordering, timestamps and reset/power epochs. Keep independent architectural checking.
6. Exercise smoke, stalls, concurrency, reset recovery and controlled checker sensitivity; record observed activity and end-of-test drain.
7. Freeze VIP version/configuration, effective checker settings, coverage scope and run evidence. Track vendor limitations and disabled checks with concrete replacement evidence.

## Detailed guidance
Read [integration procedure](references/task.md) for bring-up and review. For failures, upgrades or advanced modes, read [debug and compatibility](references/debug.md). Use [source guidance](references/sources.md) to locate authoritative product information; public overviews do not establish installed API behavior.

## Deliverables and completion
Produce the wrapper/configuration changes, connectivity map, reproducible build/run targets and an evidence-based integration report. Start with the [output template](assets/output-template.md) and applicable ledgers:
- [inventory.csv](assets/inventory.csv)
- [connections.csv](assets/connections.csv)
- [checks.csv](assets/checks.csv)
- [scenarios.csv](assets/scenarios.csv)

Missing VIP packages/licenses mean NOT_RUN or UNSUPPORTED for dependent execution. A passing vendor example alone does not prove DUT integration. Do not publish proprietary vendor sources, license files or restricted manuals with reusable skills.
