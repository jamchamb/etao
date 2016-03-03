"""Classical cryptography"""
import string


def letter_to_num(letter):
    """Return the position of letter in the English alphabet."""

    if not isinstance(letter, str):
        raise TypeError("Expected a string")

    if letter not in string.ascii_letters:
        raise ValueError("Expected a single ASCII letter")

    return ord(letter.upper()) - ord('A') + 1


def num_to_letter(num):
    """Return the letter of the English alphabet at the given position."""

    if not isinstance(num, int):
        raise TypeError("Expected an integer")

    if num < 1 or num > 26:
        raise ValueError("Expected an integer between 1 and 26 (inclusive)")

    return chr(num-1 + ord('A'))


def caesar_shift_letter(letter, shift):
    """Return the Caesar shifted letter."""

    if shift < 0:
        raise ValueError("Expected a positive shift value")
    shift %= 26

    num = letter_to_num(letter) - 1
    num = ((num + shift) % 26) + 1

    return num_to_letter(num)


def caesar_shift(text, shift):
    """Return the Caesar shifted text."""

    result = ""
    for char in text:
        if char in string.ascii_letters:
            result += caesar_shift_letter(char, shift)
        else:
            result += char
    return result


def vigenere_encrypt(plaintext, key):
    """Return the plaintext encrypted with the Vigenere cipher, using the
       given key."""

    result = ""
    key_index = 0

    for char in plaintext:
        if char in string.ascii_letters:
            shift = letter_to_num(key[key_index % len(key)]) - 1
            key_index += 1
            result += caesar_shift_letter(char, shift)
        else:
            result += char

    return result


def vigenere_decrypt(ciphertext, key):
    """Return the decrypted Vigenere ciphertext, using the given key."""

    result = ""
    key_index = 0

    for char in ciphertext:
        if char in string.ascii_letters:
            shift = 26 - (letter_to_num(key[key_index % len(key)]) - 1)
            key_index += 1
            result += caesar_shift_letter(char, shift)
        else:
            result += char

    return result
