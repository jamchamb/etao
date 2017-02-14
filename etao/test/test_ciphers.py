"""Test the cipher classes."""
import unittest
import etao


class TestBaseCipher(unittest.TestCase):
    """Test the base cipher class."""

    def test_base_encrypt(self):
        with self.assertRaises(NotImplementedError):
            etao.Cipher().encrypt('hello')

    def test_base_decrypt(self):
        with self.assertRaises(NotImplementedError):
            etao.Cipher().decrypt('hello')


class TestCaesarCipher(unittest.TestCase):
    """Test the Caesar cipher class."""

    # Caesar cipher class
    def test_caesar_class(self):
        caesar = etao.CaesarCipher(5)
        pt = 'HELLO WORLD'
        ct = caesar.encrypt(pt)
        self.assertEqual(pt, caesar.decrypt(ct))

    def test_caesar_tabula_recta(self):
        caesar = etao.CaesarCipher('F')
        pt = 'HELLO WORLD'
        ct = caesar.encrypt(pt)
        self.assertEqual(pt, caesar.decrypt(ct))


class TestVigenereCipher(unittest.TestCase):
    """Test Vigenere cipher."""

    def test_vigenere_encrypt(self):
        self.assertEqual(
            etao.VigenereCipher('LEMON').encrypt('ATTACKATDAWN'),
            'LXFOPVEFRNHR'
        )

    def test_vigenere_decrypt(self):
        self.assertEqual(
            etao.VigenereCipher('LEMON').decrypt('LXFOPVEFRNHR'),
            'ATTACKATDAWN'
        )

    def test_vigenere_encrypt_with_symbols(self):
        self.assertEqual(
            etao.VigenereCipher('LEMON').encrypt('ATTACK AT DAWN!'),
            'LXFOPV EF RNHR!'
        )

    def test_vigenere_decrypt_with_symbols(self):
        self.assertEqual(
            etao.VigenereCipher('LEMON').decrypt('LXFOPV EF RNHR!'),
            'ATTACK AT DAWN!'
        )

    def test_vigenere_encrypt_mixcase(self):
        self.assertEqual(
            etao.VigenereCipher('lEmOn').encrypt('AtTackaTdAWn'),
            'LXFOPVEFRNHR'
        )

    def test_vigenere_decrypt_mixcase(self):
        self.assertEqual(
            etao.VigenereCipher('leMoN').decrypt('lxFoPVefRNhR'),
            'ATTACKATDAWN'
        )

    def test_vigenere_bad_key_symbol(self):
        with self.assertRaises(ValueError):
            etao.VigenereCipher('LEMON!').encrypt('ATTACKATDAWN')


class TestSimpleSubstitutionCipher(unittest.TestCase):
    """Test simple substitution cipher."""

    def test_encrypt(self):
        self.assertEqual(
            etao.SimpleSubstitutionCipher("DOLPHINS").encrypt(
                "So long, and thanks for all the fish!"),
            "RJ EJGN, DGP TSDGCR IJQ DEE TSH IARS!"
        )

    def test_decrypt(self):
        self.assertEqual(
            etao.SimpleSubstitutionCipher("DOLPHINS").decrypt(
                "RJ EJGN, DGP TSDGCR IJQ DEE TSH IARS!"),
            "SO LONG, AND THANKS FOR ALL THE FISH!"
        )
