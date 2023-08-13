import unittest
from stegjson import ArrayReader
from tests.data_creator import create_dictionary_array

class ArrayReaderTest(unittest.TestCase):
    def test_reading_with_too_few_keys_fails(self):
        test_array = create_dictionary_array(10, 8)     # 8 keys is not enough
        error_regex = r"must contain at least 9 keys"
        self.assertRaisesRegex(ValueError, error_regex, lambda : ArrayReader(test_array).payload)
