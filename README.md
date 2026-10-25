# Design Verification Skills for Codex and Claude Code

Fifteen reusable skills for RTL, IP, and subsystem design verification, covering SystemVerilog/UVM, assertions, coverage, GLS/SDF, UPF low-power, CDC/RDC, protocols and verification evidence.

## Attribution

The repository structure is inspired by [VLSIT_CODEX_CLAUDE_SKILLS](https://github.com/nguyenquanicd/VLSIT_CODEX_CLAUDE_SKILLS) at commit `e9b8070303061a77524f504e858230f686abdcbf`: paired Codex/Claude skill directories, self-contained rule and reference documents, and evidence-focused workflows.

The DV instructions and project policies are independently authored. This is not an official release from the authors of the reference repository. No upstream implementation or rule text is redistributed, and RTL-specific rules have not been copied into testbench guidance.

## Skill catalog

| Skill | Purpose |
|---|---|
| `vlsit-dv-workflow` | Coordinate the verification workflow and its deliverables |
| `vlsit-dv-testplan` | Build verification plans with requirement traceability |
| `vlsit-dv-uvm-env` | Build UVM agents and environments |
| `vlsit-dv-sequences` | Develop directed and constrained-random stimulus |
| `vlsit-dv-scoreboard` | Design reference models and scoreboards |
| `vlsit-dv-sva-formal` | Develop assertions, formal checks, and vacuity checks |
| `vlsit-dv-coverage` | Define coverage models and drive coverage closure |
| `vlsit-dv-ral` | Build register models, adapters, and predictors |
| `vlsit-dv-regression` | Organize regressions and summarize run records |
| `vlsit-dv-debug` | Analyze failures and reproduce failing seeds |
| `vlsit-dv-signoff` | Review verification evidence and sign-off readiness |
| `vlsit-dv-gls` | Review and debug gate-level simulation, SDF annotation and timing/X failures |
| `vlsit-dv-upf` | Review power intent and verify isolation, retention and power transitions |
| `vlsit-dv-cdc-rdc` | Audit crossing constraints, CDC/RDC reports, protocols and waivers |
| `vlsit-dv-protocol` | Verify protocol variants, channel timing, ordering and checker activation |

## Setup and use

Clone the repository:

```bash
git clone https://github.com/Nam24-dot/DV_CODEX_CLAUDE_SKILLS.git
cd DV_CODEX_CLAUDE_SKILLS
python3 tools/validate_suite.py
```

Open this repository in Codex or Claude Code, or copy complete skill folders into your target project: `.agents/skills/` for Codex and `.claude/skills/` for Claude Code. Preserve each skill's references, assets, scripts, and agents directories. Compare existing skills before overwriting them.

The two skill trees are byte-identical. Maintain `.agents/skills` as the canonical tree and update the paired tree deliberately; `python3 tools/validate_suite.py` detects drift.

If you received the suite as a Git bundle, restore it with:

```bash
git clone DV_CODEX_CLAUDE_SKILLS.bundle DV_CODEX_CLAUDE_SKILLS
cd DV_CODEX_CLAUDE_SKILLS
python3 tools/validate_suite.py
```

Example Codex prompt:

```text
$vlsit-dv-testplan Analyze spec/fifo.md and rtl/fifo.sv. Produce a requirement-traceable verification plan; keep unspecified simultaneous push/pop behavior as an open question.
```

Example Claude Code prompt:

```text
/vlsit-dv-uvm-env Extend tb/ for top fifo using the project's installed UVM version and existing compile target. Add monitor-driven checking, reset handling and a bounded smoke test.
```

Additional prompts:

- `vlsit-dv-scoreboard`: build an in-order FIFO reference model from the supplied acceptance/reset contract; demonstrate mismatch detection.
- `vlsit-dv-sva-formal`: write stall-stability properties for the supplied ready/valid contract and check activation.
- `vlsit-dv-debug`: diagnose the attached seed/log; distinguish evidence from hypotheses and preserve the first failure.
- `vlsit-dv-signoff`: audit the supplied requirement matrix, regressions and coverage against our recorded criteria.

Provide actual project paths, the top-level module, specification, simulator, UVM version, and verification objectives. Each skill uses the available context and asks only about unresolved decisions that affect behavior.

## Conventions

- Documentation, technical instructions, code, templates, and reports are written in engineering English. Skills respond to users in their requested language.
- `DV_RULES.md` contains 20 independently authored project rules. These are not an IEEE standard or official VLSIT rules.
- Each skill includes its own rules, references, and templates. The workflow skill coordinates sibling skills when they are installed.
- PASS requires actual evidence. Missing tools must be reported as NOT_RUN or UNSUPPORTED; formal timeouts are INCONCLUSIVE. High coverage or successful skill structure checks alone do not establish sign-off readiness.
- This suite provides task guidance and metadata tools. It is not certified verification IP, a simulator, or a testbench for a specific DUT.

## Tools

Python 3.9+ and its standard library are sufficient for the included helpers.

- `python3 tools/validate_suite.py`: checks the catalog, restricted UI metadata schema, local Markdown file links throughout each skill, paired-tree equality, unique rules, and script syntax. Link anchors and remote URLs are not validated.
- `python3 .agents/skills/vlsit-dv-regression/scripts/summarize_runs.py runs.json --out summary.json`: validates and aggregates normalized run records; it does not parse simulator logs or establish correctness.
- `python3 tools/test_helpers.py`: runs synthetic positive and negative checks for the result summarizer.
- `python3 tools/test_validator.py`: checks that malformed metadata, broken nested links, missing rules, tree drift and catalog mismatches are rejected.
- `tools/skill_catalog.json`: explicit skill inventory; update it when adding or retiring a skill.

The UI validator deliberately supports this suite's three JSON-quoted `interface` strings, not arbitrary YAML. Extend its schema and tests before introducing optional policy/dependency fields.

See [VALIDATION.md](VALIDATION.md) for the validation scope, results, and limitations. The suite has not been validated against a real DUT or simulator.

## Technical sources

- [Accellera UVM implementation and compatibility notes](https://github.com/accellera-official/uvm-core)
- [Accellera UVM resources](https://www.accellera.org/downloads/standards/uvm)
- [UVM 1.2 legacy user guide](https://www.accellera.org/images/downloads/standards/uvm/uvm_users_guide_1.2.pdf)
- [Codex skill documentation](https://developers.openai.com/codex/skills)
- [Claude Code skill documentation](https://code.claude.com/docs/en/skills)

Pin the actual project tool and UVM versions. These links are references, not bundled dependencies or a promise that every simulator supports every UVM/SVA construct.

## Detailed workflows and specialist use

Each original skill now includes `references/detailed-workflow.md` and an editable `assets/review-ledger.csv`. New specialist skills include stage-by-stage references and domain-specific ledgers. Entry points route to these resources only when the task needs the detail. Templates contain headers, not fabricated PASS rows.

| Specialist | Review stages | Primary ledgers |
|---|---|---|
| GLS | PRE_SYNTH, POST_PNR without SDF, POST_PNR_SDF; artifact pairing, annotation audit and timing/X diagnosis | annotation, scenarios, violations |
| UPF | Domain/supply inventory, resolved strategies, legal transitions, isolation, retention/recovery, coverage | domains, transitions, strategies |
| CDC/RDC | Constraint coverage, crossing classification, protocol/reset analysis, triage and waivers | crossings, constraints, waivers |
| Protocol | Version/features, channel contract, legal/negative stimulus, matching, activation | channels, scenarios |

Example prompts (replace artifact paths with real project paths):

```text
$vlsit-dv-gls Review netlist/chip.v, timing/chip.sdf and logs/annotation.log against our required corner matrix. Audit annotation completeness before assessing timing-run results; preserve unmatched instances and timing-check failures.
$vlsit-dv-upf Review power/top.upf and spec/power.md. Produce domain and transition ledgers, then implement supported isolation/retention checks. Keep unknown save/restore ordering explicit.
$vlsit-dv-cdc-rdc Review reports/cdc.txt, reports/rdc.txt and constraints/ against spec/clock_reset.md. Separate setup gaps, unsafe crossings and evidence-backed waivers.
$vlsit-dv-protocol Review the supplied AXI4-Lite agent against the selected protocol issue. Exercise independent AW/W arrivals, backpressure, error responses and reset with pending transfers.
```

For Claude Code use `/vlsit-dv-gls`, `/vlsit-dv-upf`, `/vlsit-dv-cdc-rdc` or `/vlsit-dv-protocol` with the same project context. Do not assume a skill name installs simulator support, a license, protocol VIP or technology libraries.

GLS is not STA or equivalence sign-off. Power-aware simulation is not physical low-power implementation sign-off. Digital simulation does not prove analog metastability safety. Use the project's required specialist tools and record unavailable checks honestly.

See [behavioral evaluation cases](EVALUATION.md) for reproducible review scenarios and scoring criteria. These cases are provided for future model runs; their presence is not evidence that an agent passed them.

### GLS phase terminology

1. **Pre-simulation after synthesis (PRE_SYNTH):** synthesized netlist, without SDF.
2. **Post-simulation after place and route (POST_PNR):** post-PNR netlist, without SDF.
3. **Post-simulation after place and route + SDF (POST_PNR_SDF):** matching post-PNR netlist and extracted SDF, with corner-specific annotation and timing checks.

See the [phase-by-phase GLS procedure](.agents/skills/vlsit-dv-gls/references/phases.md). No-SDF runs still record actual library delays and simulator options; power-aware operation is an additional mode rather than a fourth phase.
