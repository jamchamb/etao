"""Frequency analysis, etc."""
import math
from .frequencies import ENGLISH_FREQ


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
