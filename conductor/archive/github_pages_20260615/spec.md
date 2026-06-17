# Specification: Astro Documentation & Parameter Explorer

## Purpose
Scaffold and integrate an interactive Policy Parameter Explorer into the Astro-based documentation site to enable policy analysts and researchers to search, view, and trace changes to tax rules and benefits over time.

## Requirements
- Setup a script `generate_parameters.py` to compile recursively all OpenFisca parameters into JSON format.
- Create a user-friendly parameters browser under `/explorer` in Astro Starlight using modern CSS styling.
- Integrate search functionality allowing query matching on parameter names, descriptions, or paths.
- Automatically compile and render progressive tax rate details and thresholds dynamically from the parameters database.
- Publish the generated Astro documentation site to GitHub Pages from the docs workflow.
