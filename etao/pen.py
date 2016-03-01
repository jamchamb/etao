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
    for i in range(len(text)):
        if text[i] in string.ascii_letters:
            result += caesar_shift_letter(text[i], shift)
        else:
            result += text[i]
    return result
