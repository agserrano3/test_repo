import json

def print_json_keys(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    keys = list(data.keys())

    for key in keys:
        print(key)

    return keys