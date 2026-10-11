# Coverage report contract
For each metric keep covered count, total count, exclusions, scope, build/configuration identity and report source. If a tool reports weighted coverage, preserve that definition rather than recomputing a misleading simple percentage.

Do not merge across changed bin definitions, incompatible parameter elaborations or different RTL revisions without the tool/project compatibility policy and an explicit mapping. Per-instance and type coverage are different denominators.

Closure table: bin/requirement, observed count, cause hypothesis, evidence, proposed action, owner, status. A bin hit establishes observation, not data correctness. Keep checker results alongside but distinct from the coverage percentage.
