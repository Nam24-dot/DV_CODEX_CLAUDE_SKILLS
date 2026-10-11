# Design Verification Skills for Codex and Claude Code

Bộ 11 skills cho Design Verification RTL/IP/subsystem, tập trung SystemVerilog/UVM, assertions, coverage và bằng chứng kiểm chứng. / Eleven reusable skills for RTL/IP/subsystem verification.

## Tham khảo / Attribution
Tham khảo cách tổ chức hai cây skills, tài liệu quy tắc đi kèm và báo cáo dựa trên bằng chứng của https://github.com/nguyenquanicd/VLSIT_CODEX_CLAUDE_SKILLS tại commit `e9b8070303061a77524f504e858230f686abdcbf`. Nội dung DV được viết mới; không phải bản phát hành chính thức của tác giả repository mẫu. Không sao chép bộ RTL rules để áp lên testbench.

Reference architecture: paired Codex/Claude skill directories, self-contained references and evidence-focused workflows. The DV instructions and project policy are independently authored. No upstream implementation or rule text is redistributed.

## Danh sách / Catalog
| Skill | Công việc / Purpose |
|---|---|
| `vlsit-dv-workflow` | DV Workflow |
| `vlsit-dv-testplan` | DV Test Plan |
| `vlsit-dv-uvm-env` | UVM Environment |
| `vlsit-dv-sequences` | DV Stimulus |
| `vlsit-dv-scoreboard` | DV Scoreboard |
| `vlsit-dv-sva-formal` | SVA and Formal |
| `vlsit-dv-coverage` | DV Coverage Closure |
| `vlsit-dv-ral` | UVM Register Model |
| `vlsit-dv-regression` | DV Regression |
| `vlsit-dv-debug` | DV Failure Debug |
| `vlsit-dv-signoff` | DV Sign-off Review |

## Cài và dùng / Setup and use
Mở thư mục này bằng Codex hoặc Claude Code, hoặc chép toàn bộ thư mục skill cần dùng vào project đích: `.agents/skills/` cho Codex, `.claude/skills/` cho Claude Code. Giữ nguyên references, assets, scripts và agents. Không ghi đè bản skill đang dùng nếu chưa so sánh.

Open this repository as your project, or copy complete skill folders into the target project's matching directory. The two trees are byte-identical. Maintain `.agents/skills` as canonical and update the paired tree deliberately; `python3 tools/validate_suite.py` detects drift.

Nếu nhận bộ này ở dạng Git bundle, khôi phục repository bằng:

```bash
git clone DV_CODEX_CLAUDE_SKILLS.bundle DV_CODEX_CLAUDE_SKILLS
cd DV_CODEX_CLAUDE_SKILLS
python3 tools/validate_suite.py
```

Codex prompt:
```text
$vlsit-dv-testplan Analyze spec/fifo.md and rtl/fifo.sv. Produce a requirement-traceable verification plan; keep unspecified simultaneous push/pop behavior as an open question.
```
Claude Code prompt:
```text
/vlsit-dv-uvm-env Extend tb/ for top fifo using the project's installed UVM version and existing compile target. Add monitor-driven checking, reset handling and a bounded smoke test.
```

Ví dụ tiếp theo / Additional prompts:
- `vlsit-dv-scoreboard`: build an in-order FIFO reference model from the supplied acceptance/reset contract; demonstrate mismatch detection.
- `vlsit-dv-sva-formal`: write stall-stability properties for the supplied ready/valid contract and check activation.
- `vlsit-dv-debug`: diagnose the attached seed/log; distinguish evidence from hypotheses and preserve the first failure.
- `vlsit-dv-signoff`: audit the supplied requirement matrix, regressions and coverage against our recorded criteria.

Điền đường dẫn thực tế, top, spec, simulator, UVM version và mục tiêu của project khi sử dụng. Skill sẽ tận dụng ngữ cảnh đã rõ và chỉ hỏi các quyết định còn thiếu ảnh hưởng tới hành vi.

## Quy ước / Conventions
- Technical instructions, code, templates and reports: engineering English. User communication: requested language. Hướng dẫn sử dụng: Việt/Anh.
- `DV_RULES.md`: 20 quy tắc dự án tự viết, không phải chuẩn IEEE hoặc rule chính thức của VLSIT.
- Mỗi skill độc lập có rule/reference/template đi kèm. Skill điều phối dùng các skill anh em khi đã cài.
- PASS cần bằng chứng thật. Thiếu tool là NOT_RUN/UNSUPPORTED; timeout formal là INCONCLUSIVE. Không suy ra sign-off từ coverage cao hoặc kiểm tra cấu trúc skill.
- Bộ này là hướng dẫn tác vụ và công cụ metadata; không phải VIP đã được chứng nhận, simulator, hay testbench cho một DUT cụ thể.

## Công cụ / Tools
Python 3.9+ standard library is sufficient for shipped helpers.
- `python3 tools/validate_suite.py`: metadata, local links, paired-tree equality, rule consistency and script syntax.
- `python3 .agents/skills/vlsit-dv-regression/scripts/summarize_runs.py runs.json --out summary.json`: strict validation and aggregation of normalized run records; does not parse simulator logs or establish correctness.
- `python3 tools/test_helpers.py`: synthetic positive/negative checks for the result summarizer.

## Nguồn kỹ thuật / Technical sources
- Accellera UVM implementation and compatibility notes: https://github.com/accellera-official/uvm-core
- Accellera UVM resources: https://www.accellera.org/downloads/standards/uvm
- UVM 1.2 legacy user guide: https://www.accellera.org/images/downloads/standards/uvm/uvm_users_guide_1.2.pdf
- Codex skill documentation: https://developers.openai.com/codex/skills
- Claude Code skill documentation: https://code.claude.com/docs/en/skills

Pin the actual project tool/UVM version. These links are references, not bundled dependencies or a promise that every simulator supports every UVM/SVA construct.
