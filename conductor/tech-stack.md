# Technology Stack: OpenFisca Aotearoa

## Core Languages & Runtimes
- **Python 3.11+:** Target the supported modern Python baseline used by the
  package and test suite, while remaining compatible with newer Python releases
  as dependencies permit.

## Package & Environment Management
- **UV-compatible `pyproject.toml`:** Use standards-based project metadata and
  optional development dependencies so UV can create fast, reproducible local and
  CI environments.
- **Hatch/Hatch-VCS:** Build wheels with Hatchling and derive package versions
  from Git tags.

## Core Frameworks & Libraries (Rust-Powered & Modern)
- **OpenFisca Core:** Open-source rules engine framework, targeted for upgrade to **latest stable v44+** (moving away from the legacy locked `<42` range) to leverage improved vector processing and modern API routing features.
- **Data Manipulation (Latest & Pinned):**
  - `pandas>=2.2` (Latest stable release line, moving to `polars` for new development)
  - `numpy>=2.0` (Latest NumPy 2.x for advanced vector/matrix computational speeds)
- **Data Validation & Parsing:** `pydantic v2` (Rust-backed core) for type-safe validation.
- **Logging:** `loguru` (Elegant, out-of-the-box structured logging replacing standard `logging`).
- **Serialization:** `orjson` (Fast, Rust-backed JSON library).
- **Versioning:** `hatch-vcs` or `setuptools-scm` for dynamic versioning based on Git tags.

## Static Typing, Linting & Formatting
- **basedpyright:** The feature-rich fork of `pyright`, introduced with a basic
  baseline first and intended to tighten as legacy OpenFisca code is annotated.
- **ty:** typing wrappers.
- **ruff:** Rust-backed code linter and formatter, initially enforcing Pyflakes
  correctness while the legacy codebase is migrated toward broader rule sets.
- **vale:** Prose linter to enforce editorial standards and guidelines in Markdown documentation (like `product-guidelines.md` and legislative annotations).

## Advanced Testing, Validation & Quality Assurance
- **pytest:** Test framework runner.
- **hypothesis:** Property-based testing library for edge-case test generation.
- **mutmut:** Mutation testing to audit test suite coverage.
- **schemathesis:** API fuzzing tool to automatically test the OpenFisca Web API schema for compliance and robustness.
- **behave:** BDD framework to translate legislative rules into Gherkin "Given/When/Then" specifications.
- **codecov:** Code coverage analysis.

## Performance Profiling
- **scalene:** High-performance CPU/GPU/memory profiler.
