# Specification: Release & Dependency Lifecycle Automation

## Purpose
Automate dependency upgrades and release tagging to align the project with bleeding-edge python tooling and secure maintenance.

## Requirements
- Configure Dependabot to scan python requirements (`pip` ecosystem) and GitHub Actions updates.
- Setup `hatch-vcs` version source to dynamically resolve the package version from git tags on release builds.
- Release automation must treat version tags as the source of truth, fetch enough Git history for Hatch-VCS, and remain safe before the first repository tag exists.
