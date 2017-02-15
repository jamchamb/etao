"""Test analysis functions"""
import unittest
import etao


class TestHamming(unittest.TestCase):

    def test_hamming(self):
        self.assertEqual(
            etao.hamming_distance('this is a test',
                                  'wokka wokka!!!'),
            37
        )

    def test_hamming_len_mismatch(self):
        with self.assertRaises(ValueError):
            etao.hamming_distance('abc', 'defg')


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
            etao.char_frequency('a..a!a?   b'),
            {'a': 0.75, 'b': 0.25}
        )

    def test_ngram_freq(self):
        self.assertEqual(
            etao.ngram_frequency('the', 2),
            {'th': 0.5, 'he': 0.5}
        )

    def test_ngram_freq_preserve_format(self):
        self.assertEqual(
            etao.ngram_frequency('t h.e!!', 2),
            {}
        )

    def test_ngram_freq_no_preserve_format(self):
        self.assertEqual(
            etao.ngram_frequency('t h e!!', 2, preserve_format=False),
            {'th': 0.5, 'he': 0.5}
        )

    def test_ngram_freq_symbols(self):
        self.assertEqual(
            etao.ngram_frequency('wow!', 2, only_alpha=False),
            {'wo': 1/3.0, 'ow': 1/3.0, 'w!': 1/3.0}
        )
