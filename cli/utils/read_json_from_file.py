import json

def read_json_from_file(filename: str):
    try:
        with open(filename, "rb") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Input JSON file is not in JSON format")
    except FileNotFoundError:
        print("Input JSON file does not exist")
    return None
