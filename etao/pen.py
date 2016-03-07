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


def complete_alphabet(key):
    """Complete the alphabetic key by appending unused letters
       in alphabetic order."""

    key = key.upper()

    if not key.isalpha():
        raise ValueError("The key must only contain letters")
    elif len(key) != len(set(key)):
        raise ValueError("The key must not contain duplicate letters")
    elif len(key) == 26:
        return key.upper()

    for letter in string.ascii_uppercase:
        if letter not in key:
            key += letter

    return key


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


def simple_sub_encrypt(plaintext, key):
    """Return the ciphertext produced by encrypting the given plaintext
       with the simple substitution cipher (monoalphabetic), using the
       given key.

       The key must consist of distinct letters. Unused letters will
       automatically be appended to the end of the key in alphabetic
       order."""

    # Check the key and complete it, if necessary
    key = complete_alphabet(key)

    result = ""
    for char in plaintext:
        if char in string.ascii_letters:
            char = char.upper()
            sub = key[letter_to_num(char) - 1]
            result += sub
        else:
            result += char

    return result


def simple_sub_decrypt(ciphertext, key):
    """Return the plaintext produced by decrypting the given ciphertext
       with the simple substitution cipher (monoalphabetic), using the
       given key.

       The key must consist of distinct letters. Unused letters will
       automatically be appended to the end of the key in alphabetic
       order."""

    # Check the key and complete it, if necessary
    key = complete_alphabet(key)

    result = ""
    for char in ciphertext:
        if char in string.ascii_letters:
            char = char.upper()
            sub = num_to_letter(key.index(char) + 1)
            result += sub
        else:
            result += char

    return result
