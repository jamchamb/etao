"""Utilities"""
import string


PRINTABLE = str(string.ascii_letters + string.digits +
                string.punctuation + string.whitespace).encode('ascii')


def escape_nonprintables(input_string):
    """Replace non-printable characters and line breaks in a string
       with escaped hex codes."""

    result = ''
    for char in input_string:
        char = bytes([char])
        if (char not in PRINTABLE) or \
           (char != b' ' and char.isspace()):
            result += '\\x' + char.hex()
        else:
            result += char.decode('ascii')
    return result


def contains_nonprintables(input_string):
    """Check if non-printable characters are in the string."""

    for char in input_string:
        if char not in PRINTABLE:
            return True
    return False


def preview_crack_buf(cracked, unknown_char=u"\U0001F47B"):
    """Print out array of characters where unknown values are
    represented by None"""
    preview = ''
    for j in range(len(cracked)):
        if cracked[j] is None:
            preview += unknown_char
        else:
            preview += chr(cracked[j])
    return preview
