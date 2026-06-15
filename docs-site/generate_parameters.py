import os
import yaml
import json

def parse_yaml_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def build_parameter_tree(base_dir):
    flat_parameters = []
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                
                # Construct dot-separated name: e.g. taxes.income_tax.individual_income_tax_rate
                name_parts = os.path.splitext(rel_path)[0].replace(os.sep, '.')
                
                content = parse_yaml_file(full_path)
                if content is None:
                    continue
                
                description = content.get('description', '')
                reference = content.get('reference', '')
                brackets = content.get('brackets', None)
                value = content.get('value', None)
                metadata = content.get('metadata', {})
                
                param_data = {
                    "id": name_parts,
                    "name": name_parts.split('.')[-1].replace('_', ' ').title(),
                    "path": name_parts,
                    "description": description,
                    "reference": reference,
                    "metadata": metadata,
                }
                
                if brackets:
                    param_data["type"] = "brackets"
                    param_data["brackets"] = brackets
                elif value:
                    param_data["type"] = "value"
                    param_data["values"] = value
                else:
                    # Could be nested direct values
                    param_data["type"] = "nested"
                    param_data["raw"] = content
                
                flat_parameters.append(param_data)
                
    return flat_parameters

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'openfisca_aotearoa', 'parameters'))
    print(f"Reading parameters from {base_dir}")
    flat_params = build_parameter_tree(base_dir)
    
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src', 'parameters.json'))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(flat_params, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully wrote {len(flat_params)} parameters to {output_path}")

if __name__ == '__main__':
    main()
