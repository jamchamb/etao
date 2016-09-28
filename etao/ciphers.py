"""Cipher classes"""
from .pen import caesar_shift


class Cipher:

    def __init__(self):
        pass

    def encrypt(plaintext):
        raise NotImplementedError()

    def decrypt(ciphertext):
        raise NotImplementedError()


class CaesarCipher(Cipher):

    def __init__(self, shift):
        self.shift = int(shift)

    def encrypt(self, plaintext):
        return caesar_shift(plaintext, self.shift)

    def decrypt(self, ciphertext):
        return caesar_shift(ciphertext, -self.shift)
