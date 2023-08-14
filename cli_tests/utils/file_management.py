import os
import json
from tests.data_creator import create_dictionary_array

class FileManagement:
    VALID_JSON_FILE = "valid.json"
    INVALID_JSON_FILE = "invalid.json"
    OUTPUT_JSON_FILE = "output.json"
    PAYLOAD_INPUT_FILE = "payload.txt"

    def __init__(self) -> None:
        self.original_valid_json = create_dictionary_array(1000, 9)
        self.original_payload = "hello foo bar"

    def create_test_files(self) -> None:
        with open(FileManagement.VALID_JSON_FILE, "w") as file:
            json.dump(self.original_valid_json, file)
        with open(FileManagement.INVALID_JSON_FILE, "w") as file:
            file.write("this is definitely not in json format")
        with open(FileManagement.PAYLOAD_INPUT_FILE, "w") as file:
            file.write(self.original_payload)

    def _remove_file_if_exists(self, filename: str) -> None:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

    def remove_test_files(self) -> None:
        files = [
            FileManagement.VALID_JSON_FILE,
            FileManagement.INVALID_JSON_FILE,
            FileManagement.OUTPUT_JSON_FILE,
            FileManagement.PAYLOAD_INPUT_FILE,
        ]
        for filename in files:
            self._remove_file_if_exists(filename)
