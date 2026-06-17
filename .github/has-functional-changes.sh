#! /usr/bin/env bash

set -euo pipefail

IGNORE_DIFF_ON="README.md CONTRIBUTING.md Makefile .gitignore .github/*"

if last_tagged_commit=$(git describe --tags --abbrev=0 --first-parent 2>/dev/null)
then
    diff_base=$last_tagged_commit
else
    diff_base=$(git rev-list --max-parents=0 HEAD)
fi

if git diff-index --name-only --exit-code "$diff_base" -- . $(echo " $IGNORE_DIFF_ON" | sed 's/ / :(exclude)/g')
then
    echo "No functional changes detected."
    exit 1
else
    echo "The functional files above were changed."
fi
