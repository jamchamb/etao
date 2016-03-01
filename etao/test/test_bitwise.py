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

    def test_htb64(self):
        self.assertEqual(etao.hex_to_b64('4554414f'), 'RVRBTw==')


class TestEncrypting(unittest.TestCase):

    def test_xor(self):
        self.assertEqual(
            etao.xor_bytes('Hello, world!', 'ETAO'),
            '\x0d\x31\x2d\x23\x2a\x78\x61\x38\x2a\x26\x2d\x2b\x64'
        )
