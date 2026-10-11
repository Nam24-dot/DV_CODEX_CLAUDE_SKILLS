# Evidence contract

For every artifact record source/spec revision, generation revision, configuration, assumptions and owner. Use portable paths and keep raw logs in project run directories; do not embed secrets or absolute machine-specific paths in reusable skills.

For an executable check record: check_id, requirement_ids, tool/version, UVM version where applicable, command as an argument array or exact reproducible shell command, working directory, filelist/hash, defines, parameters, seed, start/end time, exit code, status, log and rationale. Record source hashes when a Git revision cannot represent local modifications.

Separate compile/elaboration, simulation, assertion execution, formal proof and coverage analysis. A successful build establishes only that build result. A PASS simulation needs normal termination, required checker activity and no unexpected errors; inspect project-specific reporting and suppressed/demoted severities. Expected negative-test failures need exact whitelists and positive evidence that the expected detection occurred.

Report format:
1. Scope and authoritative inputs.
2. Changes/deliverables with requirement IDs.
3. Decisions and explicit assumptions.
4. Checks executed and evidence table.
5. Checks not executed and impact.
6. Open defects, exclusions and next actions.
7. Delivery status and separate human acceptance status.

Do not publish a generic sign-off threshold. Use the project's recorded acceptance criteria. Scripts shipped in this suite validate metadata or structure only, never RTL correctness.
