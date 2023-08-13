import unittest
from stegjson import ArrayWriter, ArrayReader
from tests.data_creator import create_dictionary_array
from random import randbytes, seed

class ArrayWriterTest(unittest.TestCase):
    def test_read_payload_matches_written(self):
        seed(42)
        test_array = create_dictionary_array(100, 9)
        payload = randbytes(100)
        writer = ArrayWriter(test_array, payload)
        reader = ArrayReader(writer.output)
        self.assertTrue(reader.payload.startswith(payload))

    def test_writing_multiple_bytes_per_item(self):
        # 9 bytes cannot be stored in 3-lengthed array 1 byte per item
        # but can be stored in it 3 bytes per item
        test_array = create_dictionary_array(3, 25)
        payload = bytes([0, 42, 88, 255, 17, 3, 243, 90, 123])
        writer = ArrayWriter(test_array, payload)
        reader = ArrayReader(writer.output)
        self.assertTrue(reader.payload.startswith(payload))
