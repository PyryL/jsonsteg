import unittest
import os
from cli.main import start
from cli_tests.utils.file_management import FileManagement
from cli_tests.utils.console_stub import ConsoleStub

class ReadingTest(unittest.TestCase):
    def setUp(self):
        self.console_stub = ConsoleStub()
        self.file_management = FileManagement()
        self.file_management.create_test_files()

    def tearDown(self):
        self.file_management.remove_test_files()

    def test_read_payload_matches_written(self):
        start(f'write -i helloworld {FileManagement.VALID_JSON_FILE}'.split())
        start(f'read {FileManagement.VALID_JSON_FILE}'.split(), self.console_stub)
        self.assertEqual(len(self.console_stub.prints), 1)
        self.assertTrue(self.console_stub.prints[0].startswith("helloworld"))

    def test_read_payload_to_output_file(self):
        start(f'write -i helloworld {FileManagement.VALID_JSON_FILE}'.split())
        start(f'read -o {FileManagement.PAYLOAD_OUTPUT_FILE} {FileManagement.VALID_JSON_FILE}'.split())
        with open(FileManagement.PAYLOAD_OUTPUT_FILE, "r") as file:
            self.assertTrue(file.read().startswith("helloworld"))

    def test_read_invalid_json_file_fails(self):
        start(f'read -o {FileManagement.PAYLOAD_OUTPUT_FILE} {FileManagement.INVALID_JSON_FILE}'.split())
        self.assertFalse(os.path.exists(FileManagement.PAYLOAD_OUTPUT_FILE))

    def test_read_non_existant_json_file_fails(self):
        start(f'read -o {FileManagement.PAYLOAD_OUTPUT_FILE} {FileManagement.NON_EXISTANT_FILE}'.split())
        self.assertFalse(os.path.exists(FileManagement.PAYLOAD_OUTPUT_FILE))
