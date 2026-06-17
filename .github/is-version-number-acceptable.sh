#! /usr/bin/env bash

set -euo pipefail

script_dir=$(dirname "$BASH_SOURCE")

if [[ ${GITHUB_REF#refs/heads/} == main ]]
then
    echo "No need for a version check on main."
    exit 0
fi

if ! functional_changes=$("$script_dir/has-functional-changes.sh")
then
    echo "No need for a version update."
    exit 0
fi

echo "$functional_changes"

if ! echo "$functional_changes" | grep --quiet CHANGELOG.md
then
    echo "CHANGELOG.md has not been modified, while functional changes were made."
    echo "Explain what you changed before merging this branch into main."
    echo "Look at the CONTRIBUTING.md file to learn how to write the changelog."
    exit 2
fi

echo "Package version is derived from Git tags via hatch-vcs."
