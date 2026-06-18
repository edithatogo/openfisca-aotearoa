# Evidence Manifest Schema

The evidence manifest is implemented by
`openfisca_aotearoa.evidence.EvidenceManifest`.

## Top-Level Fields

- `track`: implementation track identifier.
- `generated_at`: UTC timestamp for manifest creation.
- `references`: extracted or imported source references.
- `tool_boundaries`: current local availability and operational boundaries for
  optional evidence tools.
- `summary`: optional human-readable note.

## Reference Fields

- `reference_id`: deterministic identifier derived from source path, line, and
  match index for extracted local references.
- `source_path`: local source file or external report path.
- `line_number`: 1-based line number when the reference comes from a text file.
- `source_type`: one of `legislation`, `citation_report`, `policy_intent`,
  `oia`, or `manual`.
- `title`: optional source title.
- `citation`: optional source line or citation text.
- `url`: optional source URL.
- `retrieved_at`: optional retrieval timestamp.
- `verification_status`: one of `unverified`, `verified`, `failed`,
  `manual_review`, or `tool_unavailable`.
- `notes`: optional review notes.

## Report Rendering

`EvidenceManifest.to_markdown()` renders the same manifest as a compact
human-readable report for Conductor track evidence and manual review.
