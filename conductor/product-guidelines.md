# Product Guidelines: OpenFisca Aotearoa

## Variable Naming & Legislative Alignment
To maintain high fidelity between physical legislation and code, the project adheres to the following guidelines:
1. **Direct Translation Naming:** Variable names must match the exact wording of the legislation (e.g., `is_eligible_for_working_for_families`) to allow legal experts and policy analysts to easily read and audit the codebase.
2. **Clear Technical Conventions:** Where direct translation is overly verbose, a hybrid approach using established, clear abbreviations (e.g., `wff_eligibility` alongside detailed documentation) is permitted to keep queries readable.
3. **Traceability via Citations:** All rules must contain metadata or comments referencing the exact Act, Part, or Section of the New Zealand legislation (e.g., `income_tax_act_2007`) that they implement.

## Documentation & Quality Standards
- **Explicit Legislative Sources:** Every new variable or parameter must include a `description` field in the code linking directly to the legislation source (e.g., legislation.govt.nz).
- **Legibility:** Maintain a clear, readable structure in parameters and variables so that non-developer domain experts can verify the logic.
