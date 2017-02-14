"""Test utility functions"""
import unittest
import etao


class TestNonPrintables(unittest.TestCase):

    def test_contains_false(self):
        self.assertFalse(etao.contains_nonprintables('Hello,\tworld!\n'))

    def test_contains_true(self):
        self.assertTrue(etao.contains_nonprintables('Goodbye\x00world\xff'))

    def test_escape(self):
        self.assertEqual(
            etao.escape_nonprintables('ABCD\x00\xDE\xAD\xBE\xEF'),
            'ABCD\\x00\\xde\\xad\\xbe\\xef'
        )
