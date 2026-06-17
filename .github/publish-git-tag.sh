#! /usr/bin/env bash

set -euo pipefail

if [[ -n "${RELEASE_TAG:-}" ]]
then
    tag_name="$RELEASE_TAG"
elif [[ "${GITHUB_REF:-}" == refs/tags/* ]]
then
    tag_name="${GITHUB_REF#refs/tags/}"
elif [[ -n "${RELEASE_VERSION:-}" ]]
then
    tag_name="v${RELEASE_VERSION#v}"
else
    echo "Set RELEASE_VERSION or RELEASE_TAG, or run this from a tag ref." >&2
    exit 1
fi

version="${tag_name#v}"

if [[ ! "$version" =~ ^[0-9]+(\.[0-9]+){1,2}([a-zA-Z0-9.-]+)?$ ]]
then
    echo "Refusing invalid release version: $version" >&2
    exit 1
fi

if git rev-parse --verify --quiet "$tag_name" >/dev/null
then
    if [[ "$(git rev-list -n 1 "$tag_name")" != "$(git rev-parse HEAD)" ]]
    then
        echo "Tag $tag_name already exists on another commit." >&2
        exit 1
    fi
    echo "Tag $tag_name already exists on HEAD."
    exit 0
fi

if [[ "${DRY_RUN:-}" == "true" ]]
then
    echo "Would create and push tag $tag_name for version $version."
    exit 0
fi

git tag "$tag_name"
git push origin "$tag_name"
