"""Generate quarantined AI-assisted test candidates from reviewed prompts."""

from __future__ import annotations

import argparse
from pathlib import Path

from openfisca_aotearoa.ai_test_automation import (
    generate_offline_candidate,
    write_candidate,
)


def main() -> None:
    """Generate a deterministic candidate for human or Conductor review."""
    parser = argparse.ArgumentParser(
        description="Generate quarantined AI-assisted test candidates.",
    )
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--source-track", required=True)
    parser.add_argument("--source-document", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument(
        "--output-dir",
        default="conductor/ai_test_candidates/quarantine",
    )
    args = parser.parse_args()

    candidate = generate_offline_candidate(
        candidate_id=args.candidate_id,
        source_track=args.source_track,
        source_document=args.source_document,
        prompt=args.prompt,
    )
    scenario_path, metadata_path = write_candidate(
        candidate,
        Path(args.output_dir),
    )
    print(f"Wrote {scenario_path}")
    print(f"Wrote {metadata_path}")


if __name__ == "__main__":
    main()
