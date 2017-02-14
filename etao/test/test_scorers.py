"""Test scorer classes"""
import unittest
import etao


class TestNgramFreqScorer(unittest.TestCase):

    def test_score_identical(self):
        freq = {
            'a': 0.25, 'b': 0.25,
            'c': 0.25, 'd': 0.25
        }
        scorer = etao.NgramFrequencyScorer(freq)
        self.assertEqual(
            scorer.score('ABCD'),
            1.0
        )

    def test_score_none(self):
        freq = {'a': 1.0}
        scorer = etao.NgramFrequencyScorer(freq)
        self.assertEqual(
            scorer.score('zzzz'),
            0.0
        )

    def test_score_digrams(self):
        freq = {'th': 0.5, 'he': 0.5}
        scorer = etao.NgramFrequencyScorer(freq)
        self.assertEqual(
            scorer.score('the the'),
            1.0
        )

    def test_empty_table(self):
        with self.assertRaises(ValueError):
            etao.NgramFrequencyScorer({})

    def test_invalid_table_keylen_mismatch(self):
        with self.assertRaises(ValueError):
            etao.NgramFrequencyScorer({'ayy': .2, 'lmao': 0.3})

    def test_invalid_table_case(self):
        with self.assertRaises(ValueError):
            etao.NgramFrequencyScorer({'ayyy': .2, 'LMaO': 0.3})

    def test_score_no_text(self):
        scorer = etao.NgramFrequencyScorer({'e': 0.5})
        self.assertEqual(scorer.score(''), 0)
