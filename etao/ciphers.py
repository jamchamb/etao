"""Cipher classes"""
import string
from .pen import (caesar_shift, complete_alphabet,
                  letter_to_num, num_to_letter)


class Cipher:

    def __init__(self):
        pass

    def encrypt(self, plaintext):
        raise NotImplementedError()

    def decrypt(self, ciphertext):
        raise NotImplementedError()


class CaesarCipher(Cipher):
    """Caesar cipher. Each letter in the plaintext is substituted with
       another letter based on its alphabetic position and the secret
       numeric offset key. If an alphabetic key is provided its tabula
       recta value will be used ([A..Z] = [0..25])."""

    def __init__(self, key):
        # If a letter key is provided use its tabula recta value
        if type(key) == str and key.isalpha():
            self.shift = letter_to_num(key) - 1
        else:
            self.shift = int(key)

    def encrypt(self, plaintext):
        return caesar_shift(plaintext, self.shift)

    def decrypt(self, ciphertext):
        return caesar_shift(ciphertext, -self.shift)


class VigenereCipher(Cipher):

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        result = ""
        key_index = 0

        for char in plaintext:
            if char in string.ascii_letters:
                shift = self.key[key_index]
                result += CaesarCipher(shift).encrypt(char)
                key_index = (key_index + 1) % len(self.key)
            else:
                result += char

        return result

    def decrypt(self, ciphertext):
        result = ""
        key_index = 0

        for char in ciphertext:
            if char in string.ascii_letters:
                shift = self.key[key_index]
                result += CaesarCipher(shift).decrypt(char)
                key_index = (key_index + 1) % len(self.key)
            else:
                result += char

        return result


class SimpleSubstitutionCipher(Cipher):
    """Simple monoalphabetic substitution cipher.

       The key must consist of distinct letters. Unused letters will
       automatically be appended to the end of the key in alphabetic
       order."""

    def __init__(self, key):
        # Check the key and complete it, if necessary
        self.key = complete_alphabet(key)

    def encrypt(self, plaintext):
        result = ""
        for char in plaintext:
            if char in string.ascii_letters:
                char = char.upper()
                sub = self.key[letter_to_num(char) - 1]
                result += sub
            else:
                result += char

        return result

    def decrypt(self, ciphertext):
        result = ""
        for char in ciphertext:
            if char in string.ascii_letters:
                char = char.upper()
                sub = num_to_letter(self.key.index(char) + 1)
                result += sub
            else:
                result += char

        return result
