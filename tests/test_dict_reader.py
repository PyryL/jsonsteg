import unittest
from stegjson import DictionaryReader

class DictionaryReaderTest(unittest.TestCase):
    def setUp(self):
        data = {
            'alice': 1,
            'bob': 2,
            'jake': 10,
            'ivar': 9,
            'charlie': 3,
            'hannah': 8,
            'david': 4,
            'gabriel': 7,
            'ella': 5,
            'felix': 6,
        }
        self.reader = DictionaryReader(data)

    def test_reading_bits_from_keys(self):
        correct_bits = [0,0,1,1,0,1,0,1,0]
        assert self.reader._read_bits_from_keys() == correct_bits

    def test_payload(self):
        assert self.reader.payload == bytes([53])
