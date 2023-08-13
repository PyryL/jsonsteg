import unittest
from jsonsteg import ArrayWriter
from tests.data_creator import create_dictionary_array

class ArrayWriterTest(unittest.TestCase):
    def test_writing_does_not_alter_json_data(self):
        test_array = create_dictionary_array(10, 9)
        payload = bytes([0, 42, 88, 255])
        writer = ArrayWriter(test_array[:], payload)
        
        self.assertCountEqual(writer.output, test_array)
        for i in range(len(writer.output)):
            self.assertDictEqual(writer.output[i], test_array[i])

    def test_writing_with_too_few_keys_fails(self):
        test_array = create_dictionary_array(4, 8)     # 8 keys is not enough
        payload = bytes([0, 42, 88, 255])
        writer = ArrayWriter(test_array, payload)
        def raising_write():
            output = writer.output
        self.assertRaisesRegex(ValueError, r"must contain at least 9 keys", raising_write)
