"""Test analysis functions"""
import unittest
import etao


class TestFrequency(unittest.TestCase):

    def test_char_freq_empty(self):
        self.assertEqual(etao.char_frequency(''), {})

    def test_char_freq_ab(self):
        self.assertEqual(
            etao.char_frequency('aaab'),
            {'a': 0.75, 'b': 0.25}
        )

    def test_char_freq_only_alpha(self):
        self.assertEqual(
            etao.char_frequency('a..a!a?   b', only_alpha=True),
            {'a': 0.75, 'b': 0.25}
        )

    def test_score_identical(self):
        self.assertEqual(
            etao.score_text('ABCD',
                            freq={
                                'a': 0.25, 'b': 0.25,
                                'c': 0.25, 'd': 0.25
                            }),
            1.0
        )

    def test_score_none(self):
        self.assertEqual(
            etao.score_text('zzzz', freq={'a': 1.0}),
            0.0
        )

    def test_hamming(self):
        self.assertEqual(
            etao.hamming_distance('this is a test',
                                  'wokka wokka!!!'),
            37
        )
