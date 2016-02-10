"""General cryptography/cryptanalysis functions."""
import base64
import binascii
import string
import math


def letter_to_num(letter):
    """Return the position of letter in the English alphabet."""

    return ord(letter) - ord('A') + 1


def num_to_letter(num):
    """Return the letter of the English alphabet at the given position."""

    return chr(num-1 + ord('A'))


def hex_to_bytes(hex_string):
    """Convert a string of hexadecimal values into bytes."""

    return binascii.unhexlify(hex_string)


def bytes_to_b64(input_bytes):
    """Return base64 encoding of bytes."""

    return base64.b64encode(input_bytes)


def hex_to_b64(hex_string):
    """Return base64 encoding of bytes given in hexadecimal form."""

    return bytes_to_b64(hex_to_bytes(hex_string))


def xor_bytes(input_bytes, key_bytes):
    """XOR input bytes, repeating the XOR key as necessary."""

    result = ''
    for i in range(len(input_bytes)):
        result += chr(ord(input_bytes[i]) ^ ord(key_bytes[i % len(key_bytes)]))
    return result


def hamming_distance(left_bytes, right_bytes):
    """Get the binary Hamming distance between two sequences of bytes."""

    if len(left_bytes) != len(right_bytes):
        raise Exception("Length of both sequences must match")

    result = 0
    for i in range(len(left_bytes)):
        # Each 1 bit in the XOR represents a difference
        diff = ord(left_bytes[i]) ^ ord(right_bytes[i])
        for j in range(8):
            result += (diff >> j) & 1
    return result


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


def char_frequency(text):
    """Return a table of character frequencies in the text.
       Case insensitive."""

    text_count = {}
    for char in text:
        if char.lower() in text_count:
            text_count[char.lower()] += 1
        else:
            text_count[char.lower()] = 1

    # Get frequency for each character counted
    text_freq = {x[0]: float(x[1])/len(text) for x in text_count.items()}

    return text_freq


def cosine_similarity(left_vector, right_vector):
    """Compute cosine similarity of two vectors.

    (v1 dot v1)/{||v1||*||v2||)
    http://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists"""

    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(left_vector)):
        x = left_vector[i]
        y = right_vector[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y

    if sumxx == 0 or sumyy == 0:
        return float(0)

    return float(sumxy)/math.sqrt(sumxx*sumyy)


ENGLISH_FREQ = {
    'e': 12.702,
    't': 9.056,
    'a': 8.167,
    'o': 7.507,
    'i': 6.966,
    'n': 6.749,
    's': 6.327,
    'h': 6.094,
    'r': 5.987,
    'd': 4.253,
    'l': 4.025,
    'c': 2.782,
    'u': 2.758,
    'm': 2.406,
    'w': 2.361,
    'f': 2.228,
    'g': 2.015,
    'y': 1.974,
    'p': 1.929,
    'b': 1.492,
    'v': 0.978,
    'k': 0.772,
    'j': 0.153,
    'x': 0.150,
    'q': 0.095,
    'z': 0.074
    }


def score_text(text, freq=ENGLISH_FREQ):
    """Score how well a text matches a given frequency table."""

    if len(text) == 0:
        return 0
    if len(freq) == 0:
        raise Exception("Empty frequency table")

    for k in freq.keys():
        if k != k.lower():
            raise Exception("Only use lower-case keys for frequency table")

    text_freq = char_frequency(text)

    # Get vector for each frequency table
    text_vector = []
    freq_vector = []
    for k in freq.keys():
        text_vector.append(text_freq.get(k) or 0.0)
        freq_vector.append(freq.get(k) or 0.0)

    return cosine_similarity(text_vector, freq_vector)
