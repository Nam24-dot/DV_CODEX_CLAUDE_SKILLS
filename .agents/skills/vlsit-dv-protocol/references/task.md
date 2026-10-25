# Interface contract and protocol checks

## Define the actual protocol
Record protocol family, specification issue, endpoint role, widths, optional features, ordering model, outstanding limits, supported responses and reset behavior. A label such as 'AXI' does not identify AXI4, AXI4-Lite, AXI-Stream or optional extensions.

Use authoritative clauses for normative rules and a project contract for permitted feature subsets. Keep compliance checks distinct from implementation-specific performance guarantees. Route UVM component construction to the environment skill and reference matching to the scoreboard skill when available.

## Channel worksheet
For each channel list fields, source, sink, sampling clock, acceptance event, stability requirements, reset values and legal dependencies. Distinguish a transfer on one channel from completion of a transaction spanning multiple channels.

For valid/ready protocols, determine precisely which fields remain stable while stalled and which component owns the obligation. Do not assume a timeout or eventual READY guarantee unless the protocol/project requires it.

## Scenario design
Exercise legal ordering and delay variations independently across channels, boundary addresses/sizes, partial masks, response errors, back-to-back traffic, maximum outstanding and reset with pending requests. Preserve requested/accepted/completed counts per channel.

For negative tests, specify the violated rule, injection mechanism, exact expected checker and recovery behavior. A conforming high-level driver may prevent illegal signaling; use a scoped injection mode rather than weakening its normal contract.

## APB-oriented review
Pin the APB revision and available optional signals. Review setup/access phase progression, selected peripheral, wait states, address/control stability and response sampling. Check back-to-back accesses and read/write direction changes. Apply strobe and error semantics only to supported revisions/features.

The architectural effect of an errored access may need a project-specific definition. Do not assume every bus error guarantees no side effects. Register checking must use the specified behavior.

## AXI-oriented review
Review address/data channel independence, write-data association, beat counting, last markers, byte strobes and response dependencies against the selected AXI variant. A monitor should support legal relative arrival times rather than requiring address and data in the same cycle.

For full AXI, consider burst type/length/size, alignment, boundary rules and ID-based ordering under the selected issue and supported feature subset. Use per-ID queues where multiple outstanding requests with the same ID are legal. Do not transfer AXI3 write-interleaving assumptions into AXI4.

For AXI-Lite, retain independent address/data channel handling without importing full-AXI burst or ID machinery. Multiple outstanding support and implementation limits must come from the actual interface contract.

For AXI-Stream, use the stream specification rather than the memory-mapped AXI document. Review packet boundaries and byte qualifiers only when implemented, plus backpressure stability and stream routing/identity semantics.

## Coverage and checker sensitivity
Map protocol clauses to checks and activation evidence. Cover stalls on each channel, legal relative arrival orders, boundary cases, supported errors, outstanding depth and reset recovery. A channel bin hit does not prove end-to-end data integrity.

Inject a controlled stability violation, wrong beat/last count or response-order fault as appropriate and demonstrate the intended detector. Preserve the clean baseline and keep injected faults out of normal regression builds.

## Sources
[Arm AMBA AXI and ACE specification, issue H](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/IHI0022H_amba_axi_protocol_spec.pdf) is a reference edition, not a requirement to use issue H. Locate the exact project-selected APB/AXI/AXI-Stream document and cite applicable clauses before encoding normative assertions. This skill is not licensed protocol VIP or a conformance certification.
