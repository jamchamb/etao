"""Utilities"""
import string
import binascii

PRINTABLE = string.ascii_letters + string.digits + \
            string.punctuation + string.whitespace


def escape_nonprintables(input_string):
    """Replace non-printable characters and line breaks in a string
       with escaped hex codes."""

    result = ''
    for char in input_string:
        if (char not in PRINTABLE) or \
           (char != ' ' and char in string.whitespace):
            result += '\\x' + binascii.hexlify(char)
        else:
            result += char
    return result


def contains_nonprintables(input_string):
    """Check if non-printable characters are in the string."""

    for char in input_string:
        if char not in PRINTABLE:
            return True
    return False
