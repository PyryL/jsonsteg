import json

def read_json_from_file(filename: str, console):
    try:
        with open(filename, "rb") as file:
            return json.load(file)
    except json.JSONDecodeError:
        console.print("Input JSON file is not in JSON format")
    except FileNotFoundError:
        console.print("Input JSON file does not exist")
    return None
