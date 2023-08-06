import unittest
from stegjson import ArrayWriter
from tests.data_creator import create_dictionary_array

class ArrayWriterTest(unittest.TestCase):
    def test_writing_does_not_alter_json_data(self):
        test_array = create_dictionary_array(10, 9)
        payload = bytes([0, 42, 88, 255])
        writer = ArrayWriter(test_array[:], payload)
        
        assert len(writer.output) == len(test_array)
        for i in range(len(writer.output)):
            assert writer.output[i] == test_array[i]
