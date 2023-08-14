import jsonsteg
import argparse
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

def determine_dict_or_array(json) -> str:
    if type(json) == dict:
        return "dict"
    elif type(json) == list:
        return "array"
    else:
        return None

def read_subcommand(arguments) -> None:
    # read input JSON
    parsed_input = read_json_from_file(arguments.JSON)
    if parsed_input is None:
        return

    # determine input JSON type and read data from it
    input_type = determine_dict_or_array(parsed_input)
    if input_type == "dict":
        payload = jsonsteg.DictionaryReader(parsed_input).payload
    elif input_type == "array":
        payload = jsonsteg.ArrayReader(parsed_input).payload
    else:
        print("Input JSON file is not a list or a dictionary")
        return

    # output read payload
    if arguments.output is not None:
        with open(arguments.output, "wb") as file:
            file.write(payload)
    else:
        print(payload.decode())

def write_subcommand(arguments) -> None:
    # read input JSON
    parsed_input = read_json_from_file(arguments.JSON)
    if parsed_input is None:
        return

    # read payload
    if arguments.input is not None:
        payload = arguments.input.encode("utf-8")
    else:
        with open(arguments.input_file, "rb") as file:
            payload = file.read()

    # determine input JSON type and modify it
    input_type = determine_dict_or_array(parsed_input)
    if input_type == "dict":
        output = jsonsteg.DictionaryWriter(parsed_input, payload).output
    elif input_type == "array":
        output = jsonsteg.ArrayWriter(parsed_input, payload).output
    else:
        print("Input JSON file is not a list or a dictionary")
        return

    # output modified JSON
    with open(arguments.JSON, "w") as file:
        json.dump(output, file, ensure_ascii=False)

def start():
    parser = argparse.ArgumentParser(
        description="Write payload into JSON without modifying it",
    )
    command_subparser = parser.add_subparsers(title="operation", dest="command")

    # CLI to read data
    read_parser = command_subparser.add_parser("read", help="read written data from JSON")
    read_parser.add_argument("--output", "-o", metavar="FILE", help="A file where read data will be written (default: stdout)")
    read_parser.add_argument("JSON", help="The JSON file from which to read the data")

    write_parser = command_subparser.add_parser("write", help="write data to JSON")
    # TODO: output file instead of in-place
    write_input_group = write_parser.add_mutually_exclusive_group(required=True)
    write_input_group.add_argument("--input", "-i", help="Text to write to JSON")
    write_input_group.add_argument("--input-file", "-I", metavar="FILE", help="A file whose content to write to JSON")
    write_parser.add_argument("JSON", help="The JSON to use to store the data")

    arguments = parser.parse_args()
    if arguments.command == "read":
        read_subcommand(arguments)
    elif arguments.command == "write":
        write_subcommand(arguments)
