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
