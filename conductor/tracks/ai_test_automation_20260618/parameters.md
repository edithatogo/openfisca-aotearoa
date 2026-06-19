# Parameter Evidence

Track 20 does not change OpenFisca parameter values.

The candidate-generation workflow records source documents, prompts,
generators, timestamps, review status, reviewer identity, and review timestamp
in metadata sidecars. These metadata fields are validation inputs for the
review gate, not tax-benefit parameters.

Relevant contract:

- `CandidateMetadata.review_status` must be `accepted` before a candidate can
  enter the accepted generated-test suite.
- `CandidateMetadata.reviewer` and `CandidateMetadata.reviewed_at` are required
  for accepted, rejected, or needs-changes candidates.
