"""Frequency analysis, etc."""
import collections
import math

# Non-alphabetic ASCII characters
NON_ALPHAS = ''.join(chr(c) for c in range(256) if not chr(c).isalpha())


def char_frequency(text, only_alpha=True):
    """Return a table of character frequencies in the text.
       Case insensitive; excludes non-alphabetic characters
       by default."""

    return ngram_frequency(text, 1, only_alpha)


def ngram_frequency(text, length, only_alpha=True, preserve_format=True):
    """Return a table of n-gram frequencies in the text.
       Case insensitive; excludes non-alphabetic characters
       by default. Preserves separation of alphabetic characters by
       non-alphbetic characters by default when creating n-grams with
       a length greater than one."""

    if only_alpha and not preserve_format:
        text = text.translate(None, NON_ALPHAS)

    text = text.lower()

    # Get all substrings of desired length (n-grams)
    ngrams = [text[i:i+length] for i in range(len(text) - (length - 1))]

    # Remove n-grams containing non-alphabetic characters if only_alpha
    # is set and non-alphabetic characters weren't already removed due
    # to preserve_format
    if only_alpha and preserve_format:
        ngrams = [ngram for ngram in ngrams if ngram.isalpha()]

    ngram_count = dict(collections.Counter(ngrams))

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
