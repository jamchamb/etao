"""Test codecs"""
import unittest
import etao


class TestBaseCodec(unittest.TestCase):

    def test_base_encode(self):
        with self.assertRaises(NotImplementedError):
            etao.Codec().encode('hello')

    def test_base_decode(self):
        with self.assertRaises(NotImplementedError):
            etao.Codec().decode('hello')


class TestHexCodec(unittest.TestCase):

    def test_htb(self):
        codec = etao.HexASCIICodec()
        self.assertEqual(codec.decode('41424344'), 'ABCD')

    def test_bth(self):
        codec = etao.HexASCIICodec()
        self.assertEqual(codec.encode('ABCD'), '41424344')


class TestBase64Codec(unittest.TestCase):

    def test_btb64(self):
        codec = etao.Base64Codec()
        self.assertEqual(codec.encode('ETAOINSHRDLU'), 'RVRBT0lOU0hSRExV')

    def test_b64tb(self):
        codec = etao.Base64Codec()
        self.assertEqual(codec.decode('RVRBT0lOU0hSRExV'), 'ETAOINSHRDLU')


class TestTranscoder(unittest.TestCase):

    def test_htb64(self):
        codec = etao.Transcoder(etao.HexASCIICodec(), etao.Base64Codec())
        self.assertEqual(codec.encode('4554414f'), 'RVRBTw==')

    def test_b64th(self):
        codec = etao.Transcoder(etao.HexASCIICodec(), etao.Base64Codec())
        self.assertEqual(codec.decode('RVRBTw=='), '4554414f')


class TestBitExtract(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
