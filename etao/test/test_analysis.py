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

    def test_ngram_freq(self):
        self.assertEqual(
            etao.ngram_frequency('the', 2),
            {'th': 0.5, 'he': 0.5}
        )

    def test_ngram_freq_only_alpha(self):
        self.assertEqual(
            etao.ngram_frequency('t h e!!', 2, only_alpha=True),
            {'th': 0.5, 'he': 0.5}
        )

    def test_ngram_freq_symbols(self):
        self.assertEqual(
            etao.ngram_frequency('wow!', 2),
            {'wo': 1/3.0, 'ow': 1/3.0, 'w!': 1/3.0}
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

    def test_score_digrams(self):
        self.assertEqual(
            etao.score_text('the the',
                            freq={
                                'th': 0.5, 'he': 0.5
                            }),
            1.0
            )

    def test_hamming(self):
        self.assertEqual(
            etao.hamming_distance('this is a test',
                                  'wokka wokka!!!'),
            37
        )

    def test_score_empty_table(self):
        with self.assertRaises(ValueError):
            etao.score_text('swag', freq={})

    def test_score_invalid_table(self):
        with self.assertRaises(ValueError):
            etao.score_text('swag', freq={'ayy': .2, 'lmao': 0.3})

    def test_score_invalid_table_case(self):
        with self.assertRaises(ValueError):
            etao.score_text('swag', freq={'ayyy': .2, 'LMaO': 0.3})
