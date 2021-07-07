"""Test utility functions"""
import unittest
import etao


class TestNonPrintables(unittest.TestCase):

    def test_contains_false(self):
        self.assertFalse(etao.contains_nonprintables(b'Hello,\tworld!\n'))

    def test_contains_true(self):
        self.assertTrue(etao.contains_nonprintables(b'Goodbye\x00world\xff'))

    def test_escape(self):
        self.assertEqual(
            etao.escape_nonprintables(b'ABCD\x00\xDE\xAD\xBE\xEF'),
            'ABCD\\x00\\xde\\xad\\xbe\\xef'
        )


class TestBufferPreview(unittest.TestCase):

    def test_empty(self):
        self.assertEquals(etao.preview_crack_buf([]), '')

    def test_bytes(self):
        buf = [b'h', b'i', None]
        test = etao.preview_crack_buf(buf, unknown_char=u"\U0001F47B")
        self.assertEqual(test, u"hi\U0001F47B")

    def test_nonascii_bytes(self):
        buf = [b'\x80', b'\xff', None]
        test = etao.preview_crack_buf(buf, unknown_char=u"\U0001F47B")
        self.assertEqual(test, u"\x80\xff\U0001F47B")

    def test_ints(self):
        buf = [ord('h'), ord('i'), None]
        test = etao.preview_crack_buf(buf, unknown_char=u"\U0001F47B")
        self.assertEqual(test, u"hi\U0001F47B")

    def test_chars(self):
        buf = ['h', 'i', None]
        test = etao.preview_crack_buf(buf, unknown_char=u"\U0001F47B")
        self.assertEqual(test, u"hi\U0001F47B")

    def test_multi_bytes(self):
        with self.assertRaises(ValueError):
            buf = [b'hi', b'hello', None]
            etao.preview_crack_buf(buf)

    def test_multi_chars(self):
        with self.assertRaises(ValueError):
            buf = ['hi', 'hello', None]
            etao.preview_crack_buf(buf)

    def test_bad_ints(self):
        with self.assertRaises(ValueError):
            buf = [9000, 9001, None]
            etao.preview_crack_buf(buf)

    def test_floats(self):
        with self.assertRaises(TypeError):
            buf = [9000.0, 9001.1, None]
            etao.preview_crack_buf(buf)

    def test_not_list(self):
        with self.assertRaises(TypeError):
            etao.preview_crack_buf('hello')
