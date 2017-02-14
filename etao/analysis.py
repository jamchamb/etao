"""Frequency analysis, etc."""
import math
from .freq import ENGLISH_FREQ

# Non-alphabetic ASCII characters
NON_ALPHAS = ''.join(chr(c) for c in range(256) if not chr(c).isalpha())


def char_frequency(text, only_alpha=False):
    """Return a table of character frequencies in the text.
       Case insensitive; includes non-alphabetic characters
       by default."""

    return ngram_frequency(text, 1, only_alpha)


def ngram_frequency(text, length, only_alpha=False):
    """Return a table of n-gram frequencies in the text.
       Case insensitive; includes non-alphabetic characters
       by default."""

    if only_alpha:
        text = text.translate(None, NON_ALPHAS)

    text = text.lower()

    # Get all substrings of desired length (n-grams)
    ngrams = [text[i:i+length] for i in range(len(text) - (length - 1))]

    ngram_count = {}
    for ngram in ngrams:
        if ngram in ngram_count:
            ngram_count[ngram] += 1
        else:
            ngram_count[ngram] = 1

    # Get frequency for each character counted
    text_freq = {x[0]: float(x[1])/len(ngrams) for x in ngram_count.items()}

    return text_freq


def cosine_similarity(left_vector, right_vector):
    """Compute cosine similarity of two vectors.

    (v1 dot v1)/{||v1||*||v2||)
    http://stackoverflow.com/questions/18424228"""

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


def hamming_distance(left_bytes, right_bytes):
    """Get the binary Hamming distance between two sequences of bytes."""

    if len(left_bytes) != len(right_bytes):
        raise ValueError("Length of both sequences must match")

    result = 0
    for i in range(len(left_bytes)):
        # Each 1 bit in the XOR represents a difference
        diff = ord(left_bytes[i]) ^ ord(right_bytes[i])
        for j in range(8):
            result += (diff >> j) & 1

    return result
