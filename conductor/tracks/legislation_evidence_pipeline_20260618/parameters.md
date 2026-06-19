# Parameter Evidence

Track 19 does not change OpenFisca parameter values.

The evidence pipeline scans parameter files as local evidence inputs when a
manifest is built with paths such as:

```text
openfisca_aotearoa/parameters
```

Parameter citations are represented as `EvidenceReference` records with source
path, line number, URL, verification status, and optional citation text.
