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
    if type(cracked) is not list:
        raise TypeError('input buffer must be represented as a list')

    preview = ''
    for j in range(len(cracked)):
        cur_char = cracked[j]

        if cur_char is None:
            preview += unknown_char
        elif type(cur_char) is int:
            if cur_char >= 256:
                raise ValueError('byte value must be less than 256')
            preview += chr(cur_char)
        elif type(cur_char) is bytes:
            if len(cur_char) != 1:
                raise ValueError('must be one byte per entry')
            preview += chr(ord(cur_char))
        elif type(cur_char) is str:
            if len(cur_char) != 1:
                raise ValueError('must be one char per entry')
            preview += cur_char
        else:
            raise TypeError('unsupported character type')

    return preview
