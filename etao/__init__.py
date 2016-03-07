"""General cryptography/cryptanalysis functions."""

# Disable "unused imports" nags
# flake8: noqa

from .pen import (letter_to_num, num_to_letter,
                  complete_alphabet,
                  caesar_shift_letter, caesar_shift,
                  simple_sub_encrypt, simple_sub_decrypt,
                  vigenere_encrypt, vigenere_decrypt)
from .analysis import char_frequency, score_text, hamming_distance
from .bitwise import (bytes_to_hex, hex_to_bytes, bytes_to_b64,
                      hex_to_b64, xor_bytes)
from .util import escape_nonprintables, contains_nonprintables
