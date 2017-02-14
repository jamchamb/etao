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


class TestPKCS7PadCodec(unittest.TestCase):

    def test_encode(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.encode('YELLOW SUBMARINE'),
                         'YELLOW SUBMARINE' + '\x10'*16)

    def test_encode_nothing(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.encode(''), '\x10'*16)

    def test_decode(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.decode('YELLOW SUBMARINE' + '\x10'*16),
                         'YELLOW SUBMARINE')

    def test_decode_single_block(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.decode('YELLOW SUBMARIN\x01'),
                         'YELLOW SUBMARIN')

    def test_decode_nothing(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(IndexError):
            codec.decode('')

    def test_decode_invalid_size(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(ValueError):
            codec.decode('YELLOW SUBMARINE' + '\x10'*15)

    def test_decode_invalid_padding(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(ValueError):
            codec.decode('YELLOW SUBMARINE' + '\xFF'*16)

    def test_decode_incosistent_padding(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(ValueError):
            codec.decode('YELLOW SUBMARINE\x09' + '\x10'*15)


class TestBlockCodec(unittest.TestCase):

    def test_encode(self):
        codec = etao.BlockCodec(16)
        self.assertEqual(codec.encode('DEADBEEFDEADBEEF' * 3),
                         ['DEADBEEFDEADBEEF' for x in range(3)])

    def test_encode_nothing(self):
        codec = etao.BlockCodec(16)
        self.assertEqual(codec.encode(''), [])

    def test_decode(self):
        codec = etao.BlockCodec(5)
        blocks = ['HELLO', 'WORLD']
        self.assertEqual(codec.decode(blocks), 'HELLOWORLD')

    def test_decode_nothing(self):
        codec = etao.BlockCodec(5)
        self.assertEqual(codec.decode([]), '')
