import unittest
import os
import json
from cli.main import start
from cli_tests.utils.file_management import FileManagement

class WritingTest(unittest.TestCase):
    def setUp(self):
        self.file_management = FileManagement()
        self.file_management.create_test_files()

    def tearDown(self):
        self.file_management.remove_test_files()

    def test_cli_writing_modifies_in_place(self):
        start(f'write -i helloworld {FileManagement.VALID_JSON_FILE}'.split())
        with open(FileManagement.VALID_JSON_FILE, "r") as file:
            modified_example_content = json.load(file)
        self.assertCountEqual(self.file_management.original_valid_json, modified_example_content)
        self.assertDictEqual(self.file_management.original_valid_json[42], modified_example_content[42])
        self.assertNotEqual(list(self.file_management.original_valid_json[0].keys()), list(modified_example_content[0].keys()))

    def test_cli_writing_creates_new_file_for_output(self):
        start(f'write -i helloworld -o {FileManagement.OUTPUT_JSON_FILE} {FileManagement.VALID_JSON_FILE}'.split())
        self.assertTrue(os.path.isfile(FileManagement.OUTPUT_JSON_FILE))

    def test_cli_writing_with_invalid_json_input_fails(self):
        start(f'write -i helloworld -o {FileManagement.OUTPUT_JSON_FILE} {FileManagement.INVALID_JSON_FILE}'.split())
        self.assertFalse(os.path.isfile(FileManagement.OUTPUT_JSON_FILE))
