# Regeneration and Retirement Rules

Regenerate a candidate when:

- the source legislation, variable, parameter, or track specification changes;
- the prompt is materially improved;
- the accepted test becomes flaky or ambiguous;
- a reviewer identifies missing edge cases.

Retire an accepted generated test when:

- a hand-written test supersedes it with clearer coverage;
- the source rule is removed or moved;
- the expected result no longer traces to the recorded source document;
- the candidate metadata cannot identify the reviewer and source prompt.

Do not regenerate accepted tests automatically in CI. Regeneration is an
operator action that produces quarantined candidates for review.
