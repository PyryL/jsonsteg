import unittest
import stegjson.utils.byte_converter as converter

class ByteConverterTest(unittest.TestCase):
    def test_bytes_to_bits_empty_array(self):
        assert converter.bytes_to_bits([]) == []

    def test_bytes_to_bits_valid_input(self):
        test_bytes = bytes([97, 0, 255, 8])
        test_bits = [0,1,1,0,0,0,0,1, 0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1, 0,0,0,0,1,0,0,0]
        assert converter.bytes_to_bits(test_bytes) == test_bits

    def test_bits_to_bytes_empty_array(self):
        assert converter.bits_to_bytes([]) == bytes()

    def test_bits_to_bytes_valid_input(self):
        test_bits = [0,1,1,0,0,0,0,1, 0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1, 0,0,0,0,1,0,0,0]
        test_bytes = bytes([97, 0, 255, 8])
        assert converter.bits_to_bytes(test_bits) == test_bytes
