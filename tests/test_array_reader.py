import unittest
from stegjson import ArrayReader
from tests.data_creator import create_dictionary_array

class ArrayReaderTest(unittest.TestCase):
    def test_reading_with_too_few_keys_fails(self):
        test_array = create_dictionary_array(10, 8)     # 8 keys is not enough
        error_regex = r"must contain at least 9 keys"
        self.assertRaisesRegex(ValueError, error_regex, lambda : ArrayReader(test_array).payload)

    def test_payload_is_accessible_multiple_times(self):
        test_array = create_dictionary_array(4, 9)
        reader = ArrayReader(test_array)
        self.assertEqual(reader.payload, reader.payload)
