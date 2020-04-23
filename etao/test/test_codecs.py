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
        self.assertEqual(codec.decode('41424344'), b'ABCD')

    def test_bth(self):
        codec = etao.HexASCIICodec()
        self.assertEqual(codec.encode(b'ABCD'), '41424344')


class TestBase64Codec(unittest.TestCase):

    def test_btb64(self):
        codec = etao.Base64Codec()
        self.assertEqual(codec.encode(b'ETAOINSHRDLU'), 'RVRBT0lOU0hSRExV')

    def test_b64tb(self):
        codec = etao.Base64Codec()
        self.assertEqual(codec.decode('RVRBT0lOU0hSRExV'), b'ETAOINSHRDLU')


class TestBinASCIICodec(unittest.TestCase):

    def test_encode(self):
        codec = etao.BinASCIICodec()
        self.assertEqual(codec.encode(b'Hi'),
                         [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1])

    def test_decode(self):
        codec = etao.BinASCIICodec()
        bit_array = [int(c) for c in '0101100101101111']
        self.assertEqual(codec.decode(bit_array), b'Yo')


class TestTranscoder(unittest.TestCase):

    def test_htb64(self):
        codec = etao.Transcoder(etao.HexASCIICodec(), etao.Base64Codec())
        self.assertEqual(codec.encode('4554414f'), 'RVRBTw==')

    def test_b64th(self):
        codec = etao.Transcoder(etao.HexASCIICodec(), etao.Base64Codec())
        self.assertEqual(codec.decode('RVRBTw=='), '4554414f')


class TestBitExtract(unittest.TestCase):

    def test_bitby_str(self):
        self.assertEqual(etao.bits_to_bytes('0100100001101001'), b'Hi')

    def test_bitby_array_str(self):
        bit_char_array = [c for c in '0100100001101001']
        self.assertEqual(etao.bits_to_bytes(bit_char_array), b'Hi')

    def test_bitby_array_int(self):
        bit_array = [int(c) for c in '0100100001101001']
        self.assertEqual(etao.bits_to_bytes(bit_array), b'Hi')

    def test_bits_per_byte(self):
        self.assertEqual(etao.bits_to_bytes('1001010', bpb=7), b'J')

    def test_bits_per_byte_bad(self):
        with self.assertRaises(ValueError):
            self.assertEqual(etao.bits_to_bytes('1001010', bpb=6), b'J')

    def test_bytbi(self):
        bit_array = [int(c) for c in '0100100001101001']
        self.assertEqual(etao.bytes_to_bits(b'Hi'), bit_array)


class TestPKCS7PadCodec(unittest.TestCase):

    def test_encode(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.encode(b'YELLOW SUBMARINE'),
                         b'YELLOW SUBMARINE' + b'\x10'*16)

    def test_encode_nothing(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.encode(b''), b'\x10'*16)

    def test_decode(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.decode(b'YELLOW SUBMARINE' + b'\x10'*16),
                         b'YELLOW SUBMARINE')

    def test_decode_single_block(self):
        codec = etao.PKCS7PaddingCodec(16)
        self.assertEqual(codec.decode(b'YELLOW SUBMARIN\x01'),
                         b'YELLOW SUBMARIN')

    def test_decode_nothing(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(IndexError):
            codec.decode(b'')

    def test_decode_invalid_size(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(ValueError):
            codec.decode(b'YELLOW SUBMARINE' + b'\x10'*15)

    def test_decode_invalid_padding(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(ValueError):
            codec.decode(b'YELLOW SUBMARINE' + b'\xFF'*16)

    def test_decode_incosistent_padding(self):
        codec = etao.PKCS7PaddingCodec(16)
        with self.assertRaises(ValueError):
            codec.decode(b'YELLOW SUBMARINE\x09' + b'\x10'*15)


class TestBlockCodec(unittest.TestCase):

    def test_encode(self):
        codec = etao.BlockCodec(16)
        self.assertEqual(codec.encode(b'DEADBEEFDEADBEEF' * 3),
                         [b'DEADBEEFDEADBEEF' for x in range(3)])

    def test_encode_nothing(self):
        codec = etao.BlockCodec(16)
        self.assertEqual(codec.encode(b''), [])

    def test_decode(self):
        codec = etao.BlockCodec(5)
        blocks = [b'HELLO', b'WORLD']
        self.assertEqual(codec.decode(blocks), b'HELLOWORLD')

    def test_decode_nothing(self):
        codec = etao.BlockCodec(5)
        self.assertEqual(codec.decode([]), b'')
