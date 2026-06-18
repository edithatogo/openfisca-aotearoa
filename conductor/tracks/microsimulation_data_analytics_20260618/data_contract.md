# Microsimulation Data Contract

Generated: 2026-06-18

## Purpose

This contract defines the small JSON surface used to pass fixture-sized or
survey-derived population cohorts into OpenFisca Aotearoa without vendoring
large datasets.

## Cohort Input

```json
{
  "period": "2025-01-01",
  "variables": ["age"],
  "people": [
    {
      "id": "person_a",
      "variables": {
        "date_of_birth": {
          "ETERNITY": "1995-01-01"
        }
      }
    }
  ],
  "families": [
    {
      "id": "family_a",
      "principal": "person_a",
      "children": []
    }
  ],
  "source": "fixture"
}
```

## Required Fields

- `period`: OpenFisca calculation period such as `2025` or `2025-01-01`.
- `variables`: non-empty list of OpenFisca variables to calculate.
- `people`: non-empty list of person records.
- `people[].id`: stable non-empty person identifier.
- `people[].variables`: OpenFisca input variables for the person.

## Optional Fields

- `families`: family relationship records. When omitted, the runner can fall
  back to the existing synthetic family behavior.
- `source`: provenance label such as `fixture`, `open_social_data`, or a local
  dataset name.

## Validation Rules

- Person IDs must be unique.
- Family IDs must be unique.
- Family principals and children must refer to known person IDs.
- Variables must be non-empty.
- Large dataset extracts must be bounded by the runner before OpenFisca
  execution.

## Output

```json
{
  "period": "2025-01-01",
  "variables": ["age"],
  "records": [
    {
      "id": "person_a",
      "age": 30
    }
  ]
}
```

The output records preserve the simulator's row order and are suitable for JSON
or CSV export before optional analytics processing.
