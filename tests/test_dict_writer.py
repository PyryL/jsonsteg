import unittest
from jsonsteg import DictionaryWriter
from tests.data_creator import create_dictionary

class DictionaryWriterTest(unittest.TestCase):
    def setUp(self):
        data = create_dictionary(10)
        payload = bytes([53])
        self.writer = DictionaryWriter(data, payload)

    def test_output(self):
        correct_output = {
            '01': 'item 1', '02': 'item 2', '10': 'item 10', '09': 'item 9',
            '03': 'item 3', '08': 'item 8', '04': 'item 4', '07': 'item 7',
            '05': 'item 5', '06': 'item 6',
        }
        self.assertListEqual(list(self.writer.output.keys()), list(correct_output.keys()))
        self.assertListEqual(list(self.writer.output.values()), list(correct_output.values()))
