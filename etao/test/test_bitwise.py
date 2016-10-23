"""Test bit/byte functions"""
import unittest
import etao


class TestEncoding(unittest.TestCase):

    def test_htb(self):
        self.assertEqual(etao.hex_to_bytes('41424344'), 'ABCD')

    def test_bth(self):
        self.assertEqual(etao.bytes_to_hex('ABCD'), '41424344')

    def test_btb64(self):
        self.assertEqual(etao.bytes_to_b64('ETAOINSHRDLU'), 'RVRBT0lOU0hSRExV')

    def test_b64tb(self):
        self.assertEqual(etao.b64_to_bytes('RVRBT0lOU0hSRExV'), 'ETAOINSHRDLU')

    def test_htb64(self):
        self.assertEqual(etao.hex_to_b64('4554414f'), 'RVRBTw==')

    def test_b64th(self):
        self.assertEqual(etao.b64_to_hex('RVRBTw=='), '4554414f')

    def test_bitby_str(self):
        self.assertEqual(etao.bits_to_bytes('0100100001101001'), 'Hi')

    def test_bitby_array_str(self):
        bit_char_array = [c for c in '0100100001101001']
        self.assertEqual(etao.bits_to_bytes(bit_char_array), 'Hi')

    def test_bitby_array_int(self):
        bit_array = [int(c) for c in '0100100001101001']
        self.assertEqual(etao.bits_to_bytes(bit_array), 'Hi')

    def test_bits_per_byte(self):
        self.assertEqual(etao.bits_to_bytes('1001010', bpb=7), 'J')

    def test_bits_per_byte_bad(self):
        with self.assertRaises(ValueError):
            self.assertEqual(etao.bits_to_bytes('1001010', bpb=6), 'J')

    def test_bytbi(self):
        bit_array = [int(c) for c in '0100100001101001']
        self.assertEqual(etao.bytes_to_bits('Hi'), bit_array)


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

if __name__ == "__main__":
    unittest.main()
