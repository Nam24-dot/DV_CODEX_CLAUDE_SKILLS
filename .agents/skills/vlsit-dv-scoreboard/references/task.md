# Matching and diagnostics
Record expected and observed ID, epoch, payload, byte enables, status, time and requirement ID. Keep first mismatch context, nearby transactions and outstanding queue/map state.

For in-order pipelines, model accepted input before or after same-edge output comparison according to documented latency, especially zero-latency bypass. For out-of-order traffic, an associative map by ID alone is insufficient when IDs may have multiple ordered outstanding transactions; use a per-ID queue where required.

A model self-test should include hand-calculated expected values, reset during pending traffic and an intentional corruption. Passing identical DUT/model algorithms is weaker than an independent behavioral model and must be described as such.
