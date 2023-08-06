import unittest
from random import randint, shuffle, randbytes, seed
from stegjson import DictionaryWriter, DictionaryReader

def rand_dict():
    keys = list(range(1, 1000))
    shuffle(keys)
    return { k: randint(100, 1000) for k in keys }

class DictTest(unittest.TestCase):
    def setUp(self):
        seed(42)
        self.dictionary = rand_dict()
        self.payload = randbytes(89)
        self.writer = DictionaryWriter(self.dictionary, self.payload)
        self.reader = DictionaryReader(self.writer.output)

    def test_read_payload_matches_written_payload(self):
        self.assertTrue(self.reader.payload.startswith(self.payload))

    def test_writing_does_not_lose_keys(self):
        self.assertListEqual(sorted(self.dictionary.keys()), sorted(self.writer.output.keys()))
