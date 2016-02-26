"""Utilities"""
import string
import binascii


def escape_nonprintables(input_string):
    """Replace non-printable characters and line breaks in a string
       with escaped hex codes."""

    result = ''
    printable = string.ascii_letters + string.digits + string.punctuation + ' '
    for char in input_string:
        if char not in printable:
            result += '\\x' + binascii.hexlify(char)
        else:
            result += char
    return result


def contains_nonprintables(input_string):
    """Check if non-printable characters are in the string."""

    for char in input_string:
        if char not in string.printable:
            return True
    return False
