import json
import os
from datetime import date
from pathlib import Path
from typing import Any

import yaml


def parse_yaml_file(filepath: str) -> dict[str, Any] | None:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
    except Exception as error:
        print(f"Error parsing {filepath}: {error}")
        return None

    return content if isinstance(content, dict) else None


def normalise_for_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            str(normalise_for_json(key)): normalise_for_json(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [normalise_for_json(item) for item in value]
    if isinstance(value, date):
        return value.isoformat()
    return value


def build_parameter_tree(base_dir: str) -> list[dict[str, Any]]:
    flat_parameters = []

    for root, _dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith((".yaml", ".yml")):
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            path = os.path.splitext(rel_path)[0].replace(os.sep, ".")

            content = parse_yaml_file(full_path)
            if content is None:
                continue

            param_data = {
                "id": path,
                "name": path.split(".")[-1].replace("_", " ").title(),
                "path": path,
                "description": normalise_for_json(content.get("description", "")),
                "reference": normalise_for_json(content.get("reference", "")),
                "metadata": normalise_for_json(content.get("metadata", {})),
            }

            if "brackets" in content:
                param_data["type"] = "brackets"
                param_data["brackets"] = normalise_for_json(content["brackets"])
            elif "values" in content or "value" in content:
                param_data["type"] = "value"
                param_data["values"] = normalise_for_json(
                    content.get("values", content.get("value")),
                )
            else:
                param_data["type"] = "nested"
                param_data["raw"] = normalise_for_json(content)

            flat_parameters.append(param_data)

    flat_parameters.sort(key=lambda param: param["path"])
    return flat_parameters


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent / "openfisca_aotearoa" / "parameters"
    output_path = script_dir / "public" / "parameters.json"

    print(f"Reading parameters from {base_dir}")
    flat_params = build_parameter_tree(str(base_dir))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(flat_params, f, indent=2, ensure_ascii=False)

    print(f"Successfully wrote {len(flat_params)} parameters to {output_path}")


if __name__ == "__main__":
    main()
