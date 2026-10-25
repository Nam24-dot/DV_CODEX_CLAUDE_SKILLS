# Suite validation record

## Expansion review - 2026-10-25

The working-tree expansion adds detailed workflows and review ledgers to the original 11 skills, plus GLS/SDF, UPF low-power, CDC/RDC and protocol skills. GLS follows PRE_SYNTH, POST_PNR without SDF and POST_PNR_SDF, with phase-specific procedures and evidence fields. There are now 15 skills and 135 files in each paired tree.

Executed checks for this expansion:
- `tools/validate_suite.py`: 15 skills per tool, 135 files per tree, zero structural errors.
- `tools/test_helpers.py`: three test methods passed; normalized-claim helper behavior only.
- `tools/test_validator.py`: six mutation/baseline test methods passed, covering broken nested links, malformed UI metadata, catalog mismatch, paired-tree drift and missing rules.
- Environment-provided skill-creator `quick_validate.py`: all 30 SKILL.md copies passed. PyYAML also parsed all 30 UI metadata files. PyYAML was installed temporarily for this check, not added as a suite runtime dependency. Temporary-library cleanup failed because Windows held the loaded native module; the subsequent cleanup command was blocked by execution policy. Validation itself completed with no failures.
- `git diff --check`: passed for tracked changes.

The structural validator uses an explicit catalog and checks this repository's restricted interface-only metadata syntax. It is not a full YAML parser, and it does not validate remote links or Markdown anchors. Templates contain empty ledgers, not example verification results. Behavioral scenarios in EVALUATION.md are provided but have not been run as model evaluations for this expansion.

No actual GLS, SDF annotation, UPF simulation, CDC/RDC analysis, protocol simulation, UVM runtime or formal engine was executed for this expansion. The technical workflows require project artifacts and compatible licensed/free tools as applicable. The earlier validation below is historical and must not be read as validation of the new skills.

## Original 11-skill baseline (historical)

## Scope
This review validates the skill suite and its metadata helper, not a hardware design. No DUT, simulator, UVM runtime, formal engine or license was supplied. No compile, elaboration, simulation, formal proof or coverage measurement was performed.

## Executed checks
| Check | Result | Scope |
|---|---|---|
| skill-creator quick_validate.py | PASS | All 22 SKILL.md copies, 11 per tool |
| tools/validate_suite.py | PASS | 11 skills per tree, 75 files per tree, paired content equality, links, 20-rule consistency, metadata and Python syntax |
| tools/test_helpers.py | PASS | Three test methods with positive/negative subcases: mixed statuses, invalid records, CLI round trip, malformed JSON, output overwrite refusal |
| Test-plan forward exercise | PASS for inspected behavior | Fresh agent loaded dv-testplan; produced a FIFO requirement/scenario map and surfaced unknown acceptance, simultaneous operations, output timing and reset precedence |
| Sign-off forward exercise | PASS for inspected behavior | Fresh agent loaded dv-signoff; blocked acceptance for missing reset/configuration runs, disabled checking, missing coverage denominator and inconclusive formal result |

The forward exercises used task-local skill paths and problem statements; they were not supplied an expected answer. Their outputs were reviewed manually. They did not execute hardware checks and are not broad statistical evaluations of model behavior.

## Reproduction
```bash
python3 tools/validate_suite.py
python3 tools/test_helpers.py
```
The official skill-creator validator is an environment-provided tool and is not redistributed. The self-contained suite validator uses Python standard library only.

## Forward exercise inputs
1. Synchronous FIFO, width 8, depth 4, active-low synchronous reset empties it, push/pop accepted on rising edges, empty/full flags, FIFO output order. No RTL or additional specification. Request a compact traceable plan.
2. Acceptance requires all functional requirements and required configurations checked. R1 reported passing; R2 reset-with-pending test drafted but unrun. depth4 tested, depth8 required but unrun. 100/100 reported passes, 99% coverage without denominator/exclusions, scoreboard disabled in 10 runs, formal timeout at depth20, no waivers or approver. Request readiness review.

## Limits and integration actions
- Validate generated UVM/SVA code on the target simulator and pinned library version before project use.
- These are independent project policy and workflow instructions, not IEEE conformance certification or official VLSIT content.
- At the time of the original baseline check, the suite had not been installed into a running Codex/Claude session or published to GitHub. The original repository was subsequently published; this historical check does not establish installation or execution of the expanded skills.
- The environment's personal-skills Git pointer referenced an unavailable backing repository, so automatic Skills-page commit/push could not be completed. The portable repository preserves the work in its own Git history.
