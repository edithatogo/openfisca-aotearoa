# TestSprite Evaluation

## Local Availability

Local checks on 2026-06-18:

- `where testsprite`: not found.
- `where TestSprite`: not found.
- `where npx`: available.

## Default Decision

TestSprite is treated as an optional generator, not a default CI dependency.
The repository now supports an offline deterministic candidate generator in
`scripts/generate_ai_test_candidates.py` so review gates can be tested without
network access, service credentials, or a TestSprite licence.

## CI Suitability

Default CI must not call network-only AI services. CI instead validates:

- candidate metadata contracts;
- quarantine rejection gates;
- accepted generated-test fixtures;
- deterministic execution of accepted generated scenarios.

If TestSprite is later installed and licensed, generated output must still land
in the quarantine folder first and pass the same metadata and review gate before
promotion.
