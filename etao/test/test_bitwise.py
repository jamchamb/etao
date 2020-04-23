"""Test bit/byte functions"""
import unittest
import etao


class TestBitExtraction(unittest.TestCase):

    def test_get_bit_lsb(self):
        self.assertEqual(etao.get_bit(128, 0), 0)

    def test_get_bit_msb(self):
        self.assertEqual(etao.get_bit(128, 7), 1)

    def test_get_bit_char(self):
        self.assertEqual(etao.get_bit('A', 0), 1)

    def test_get_bit_byte(self):
        self.assertEqual(etao.get_bit(b'A', 0), 1)

    def test_whole_byte(self):
        get_bits = [etao.get_bit(0xA5, i) for i in range(7, -1, -1)]
        all_bits = [1, 0, 1, 0, 0, 1, 0, 1]
        self.assertEqual(all_bits, get_bits)

    def test_get_bit_over_255(self):
        with self.assertRaises(ValueError):
            etao.get_bit(256, 0)

    def test_get_bit_under_min(self):
        with self.assertRaises(ValueError):
            etao.get_bit(0, -1)

    def test_get_bit_over_max(self):
        with self.assertRaises(ValueError):
            etao.get_bit(0, 8)

    def test_get_bit_string(self):
        with self.assertRaises(ValueError):
            etao.get_bit(b'hi', 0)

    def test_get_bit_bad_type(self):
        with self.assertRaises(TypeError):
            etao.get_bit(None, 0)

    def test_get_bits(self):
        bit_array = [int(x) for x in '01001010']
        self.assertEqual(etao.get_bits(b'J'), bit_array)


class TestEncrypting(unittest.TestCase):

    def test_xor(self):
        self.assertEqual(
            etao.xor_bytes(b'Hello, world!', b'ETAO'),
            b'\x0d\x31\x2d\x23\x2a\x78\x61\x38\x2a\x26\x2d\x2b\x64'
        )
