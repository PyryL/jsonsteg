from cli.utils.determine_json_type import determine_dict_or_array
from cli.utils.read_json_from_file import read_json_from_file
from jsonsteg import DictionaryWriter, ArrayWriter
import json

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
        output = DictionaryWriter(parsed_input, payload).output
    elif input_type == "array":
        output = ArrayWriter(parsed_input, payload).output
    else:
        print("Input JSON file is not a list or a dictionary")
        return

    # output modified JSON
    output_filename = arguments.JSON if arguments.output is None else arguments.output
    with open(output_filename, "w") as file:
        json.dump(output, file, ensure_ascii=False)
