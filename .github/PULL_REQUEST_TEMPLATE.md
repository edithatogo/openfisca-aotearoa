# Pull Request Template

## Description
Provide a summary of the changes and the context/rationale.

## Reference Legislation
- **Physical Act/Regulation:** [e.g., Social Security Act 2018]
- **Section(s):** [e.g., Section 10]
- **Citation Tooling:** Verified using `sourceright`? Yes/No

## Quality Gate Checklist
Before merging, please ensure you have completed the following checks:
- [ ] **Tests Pass:** All multi-tier test suites pass under strict settings (`-W error`).
- [ ] **Coverage:** Test coverage meets or exceeds **>90%** on new files.
- [ ] **Linting & Formatting:** `ruff` checks and formats pass without warnings.
- [ ] **Strict Typing:** `basedpyright` type check completes with zero errors.
- [ ] **Complexity Guard:** `Complexipy` checks indicate cognitive complexity is below the threshold of **15**.
- [ ] **Documentation:** Descriptions match actual legislative texts and references are updated.
- [ ] **Git Notes:** Task summary notes are attached to the commits.
