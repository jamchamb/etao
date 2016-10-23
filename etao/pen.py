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

    while shift < 0:
        shift += 26
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
