# General cryptography/cryptanalysis functions
import base64
import binascii
import string
import math

def letter_to_num(letter):
    return ord(letter) - ord('A') + 1

def num_to_letter(num):
    return chr(num-1 + ord('A'))

def hex_to_bytes(s):
    return binascii.unhexlify(s)

def bytes_to_b64(b):
    return base64.b64encode(b)

def hex_to_b64(s):
    return bytes_to_b64(hex_to_bytes(s))

def xor_bytes(b1, b2):
    '''XOR bytes, repeating b2 as necessary'''
    result = ''
    for i in range(len(b1)):
        result += chr(ord(b1[i]) ^ ord(b2[i%len(b2)]))
    return result

def hamming_distance(b1, b2):
    '''Get Hamming distance for two sequences of bytes'''
    if len(b1) != len(b2):
        raise Exception("Length of both sequences must match")

    result = 0
    for i in range(len(b1)):
        c1 = ord(b1[i])
        c2 = ord(b2[i])
        # Each 1 bit represents a difference
        diff = c1^c2
        for j in range(8):
            result += (diff >> j) & 1
    return result

def escape_nonprintables(s):
    '''Print hex codes for non-printable characters and line breaks'''
    result = ''
    printable = string.ascii_letters + string.digits + string.punctuation + ' '
    for c in s:
        if c not in printable:
            result += '\\x' + binascii.hexlify(c)
        else:
            result += c
    return result

def contains_nonprintables(s):
    '''Check if non-printable characters are in the string'''
    for c in s:
        if c not in string.printable:
            return True
    return False

def char_frequency(text):
    # Count character occurrences
    text_count = {}
    for c in text:
        if c.lower() in text_count:
            text_count[c.lower()] += 1
        else:
            text_count[c.lower()] = 1

    # Get frequency for each character counted
    text_freq = {x[0]: float(x[1])/len(text) for x in text_count.items()}

    return text_freq

def cosine_similarity(v1, v2):
    '''compute cosine similarity of v1 to v2: (v1 dot v1)/{||v1||*||v2||)
    http://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists'''
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    if sumxx == 0 or sumyy == 0:
        return float(0)
    return float(sumxy)/math.sqrt(sumxx*sumyy)

english_freq = {
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

def score_text(text, freq=english_freq):
    if len(text) == 0:
        return 0
    if len(freq) == 0:
        raise Exception("Empty frequency table")

    for k in freq.keys():
        if k != k.lower():
            raise Exception("Only use lower-case keys for frequency table")

    text_freq = char_frequency(text)

    # Get vector for each frequency table
    v1 = []
    v2 = []
    for k in freq.keys():
        v1.append(text_freq.get(k) or 0.0)
        v2.append(freq.get(k) or 0.0)

    return cosine_similarity(v1, v2)
