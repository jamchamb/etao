"""Test the classical cryptography functions."""
import unittest
import etao


class TestLetterNum(unittest.TestCase):
    """Test letter/number conversion."""

    # Number to letter section
    def test_ntl_first(self):
        self.assertEqual(etao.num_to_letter(1), 'A')

    def test_ntl_last(self):
        self.assertEqual(etao.num_to_letter(26), 'Z')

    def test_ntl_invalid_index_before(self):
        with self.assertRaises(ValueError):
            etao.num_to_letter(0)

    def test_ntl_invalid_index_after(self):
        with self.assertRaises(ValueError):
            etao.num_to_letter(27)

    def test_ntl_invalid_type(self):
        with self.assertRaises(TypeError):
            etao.num_to_letter('A')

    # Letter to number section
    def test_ltn_first(self):
        self.assertEqual(etao.letter_to_num('A'), 1)

    def test_ltn_last(self):
        self.assertEqual(etao.letter_to_num('Z'), 26)

    def test_ltn_invalid_value(self):
        with self.assertRaises(ValueError):
            etao.letter_to_num('!')

    def test_ltn_invalid_multiple_letters(self):
        with self.assertRaises(ValueError):
            etao.letter_to_num('AA')

    def test_ltn_invalid_type(self):
        with self.assertRaises(TypeError):
            etao.letter_to_num(1)


class TestCaesar(unittest.TestCase):
    """Test Caesar cipher."""

    # Single letter shift section
    def test_shift_letter_min(self):
        self.assertEqual(etao.caesar_shift_letter('A', 1), 'B')

    def test_shift_letter_max(self):
        self.assertEqual(etao.caesar_shift_letter('A', 25), 'Z')

    def test_shift_letter_none(self):
        self.assertEqual(etao.caesar_shift_letter('A', 0), 'A')

    def test_shift_letter_full(self):
        self.assertEqual(etao.caesar_shift_letter('A', 26), 'A')

    def test_shift_letter_negative(self):
        self.assertEqual(etao.caesar_shift_letter('A', -1), 'Z')

    # Full text shift section
    def test_shift_text_min(self):
        self.assertEqual(etao.caesar_shift('ABCD', 1), 'BCDE')

    def test_shift_text_max(self):
        self.assertEqual(etao.caesar_shift('ABCD', 25), 'ZABC')

    def test_shift_with_symbols(self):
        self.assertEqual(etao.caesar_shift('A. B!', 2), 'C. D!')

    def test_shift_text_invalid_type(self):
        with self.assertRaises(TypeError):
            etao.caesar_shift(123, 0)


class TestCompleteAlphabet(unittest.TestCase):
    """Test alphabet key completion."""

    def test_complete(self):
        self.assertEqual(
            etao.complete_alphabet("ZEBRAS"),
            "ZEBRASCDFGHIJKLMNOPQTUVWXY"
        )

    def test_already_complete(self):
        self.assertEqual(
            etao.complete_alphabet("ZEBRASCDFGHIJKLMNOPQTUVWXY"),
            "ZEBRASCDFGHIJKLMNOPQTUVWXY"
        )

    def test_non_alpha(self):
        with self.assertRaises(ValueError):
            etao.complete_alphabet("ABC123")

    def test_duplicate_letters(self):
        with self.assertRaises(ValueError):
            etao.complete_alphabet("ABCZZZZ")
