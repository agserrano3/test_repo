import json

def print_json_keys(data, parent_key=""):
    keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keys.append(full_key)
            keys.extend(print_json_keys(value, full_key))
    elif isinstance(data, list):
        for index, value in enumerate(data):
            full_key = f"{parent_key}[{index}]"
            keys.append(full_key)
            keys.extend(print_json_keys(value, full_key))

    return keys