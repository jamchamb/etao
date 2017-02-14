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
            etao.get_bit("hi", 0)

    def test_get_bit_bad_type(self):
        with self.assertRaises(TypeError):
            etao.get_bit(None, 0)

    def test_get_bits(self):
        bit_array = [int(x) for x in '01001010']
        self.assertEqual(etao.get_bits('J'), bit_array)


class TestEncrypting(unittest.TestCase):

    def test_xor(self):
        self.assertEqual(
            etao.xor_bytes('Hello, world!', 'ETAO'),
            '\x0d\x31\x2d\x23\x2a\x78\x61\x38\x2a\x26\x2d\x2b\x64'
        )
