import unittest
from random import randbytes, seed
from jsonsteg import DictionaryWriter, DictionaryReader
from tests.data_creator import create_dictionary

class DictTest(unittest.TestCase):
    def setUp(self):
        seed(42)
        self.dictionary = create_dictionary(1000)
        self.payload = randbytes(89)
        self.writer = DictionaryWriter(self.dictionary, self.payload)
        self.reader = DictionaryReader(self.writer.output)

    def test_read_payload_matches_written_payload(self):
        self.assertTrue(self.reader.payload.startswith(self.payload))

    def test_writing_does_not_lose_keys(self):
        self.assertListEqual(sorted(self.dictionary.keys()), sorted(self.writer.output.keys()))
