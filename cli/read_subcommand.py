from jsonsteg import ArrayReader, DictionaryReader
from cli.utils.read_json_from_file import read_json_from_file
from cli.utils.determine_json_type import determine_dict_or_array
import json

def read_subcommand(arguments) -> None:
    # read input JSON
    parsed_input = read_json_from_file(arguments.JSON)
    if parsed_input is None:
        return

    # determine input JSON type and read data from it
    input_type = determine_dict_or_array(parsed_input)
    if input_type == "dict":
        payload = DictionaryReader(parsed_input).payload
    elif input_type == "array":
        payload = ArrayReader(parsed_input).payload
    else:
        print("Input JSON file is not a list or a dictionary")
        return

    # output read payload
    if arguments.output is not None:
        with open(arguments.output, "wb") as file:
            file.write(payload)
    else:
        print(payload.decode())
