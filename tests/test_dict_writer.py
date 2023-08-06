import unittest
from stegjson import DictionaryWriter

class DictionaryWriterTest(unittest.TestCase):
    def setUp(self):
        data = {
            'alice': 1,
            'bob': 2,
            'charlie': 3,
            'david': 4,
            'ella': 5,
            'felix': 6,
            'gabriel': 7,
            'hannah': 8,
            'ivar': 9,
            'jake': 10,
        }
        payload = bytes([53])
        self.writer = DictionaryWriter(data, payload)

    def test_keys_reordering(self):
        correct_order = [
            'alice', 'bob', 'jake', 'ivar', 'charlie',
            'hannah', 'david', 'gabriel', 'ella', 'felix'
        ]
        self.assertListEqual(self.writer._reorder_keys(), correct_order)

    def test_output(self):
        correct_output = {
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
        self.assertListEqual(list(self.writer.output.keys()), list(correct_output.keys()))
