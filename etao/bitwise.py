"""Bits & bytes"""
import base64
import binascii


def hex_to_bytes(hex_string):
    """Convert a string of hexadecimal values into bytes."""

    return binascii.unhexlify(hex_string)


def bytes_to_hex(byte_string):
    """Convert a string of bytes into hexadecimal string representation."""

    return binascii.hexlify(byte_string)


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
