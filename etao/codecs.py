"""Encoder/decoder classes"""
import base64
import binascii
from .bitwise import (bytes_to_bits, bits_to_bytes)


class Codec:

    def __init__(self):
        pass

    def encode(self, data):
        raise NotImplementedError()

    def decode(self, data):
        raise NotImplementedError()


class Transcoder(Codec):
    """Translate from 'incodec' encoded data to 'outcodec' encoded data"""

    def __init__(self, incodec, outcodec):
        self.incodec = incodec
        self.outcodec = outcodec

    def encode(self, data):
        return self.outcodec.encode(self.incodec.decode(data))

    def decode(self, data):
        return self.incodec.encode(self.outcodec.decode(data))


class BinASCIICodec(Codec):

    def __init__(self):
        pass

    def encode(self, data):
        return bytes_to_bits(data)

    def decode(self, data):
        return bits_to_bytes(data)


class HexASCIICodec(Codec):

    def __init__(self):
        pass

    def encode(self, data):
        return binascii.hexlify(data).decode()

    def decode(self, data):
        return binascii.unhexlify(data)


class Base64Codec(Codec):

    def __init__(self):
        pass

    def encode(self, data):
        return base64.b64encode(data).decode()

    def decode(self, data):
        return base64.b64decode(data)


class PKCS7PaddingCodec(Codec):

    def __init__(self, block_size):
        self.block_size = block_size

    def encode(self, data):
        pads = self.block_size - (len(data) % self.block_size)
        return data + (bytes([pads]) * pads)

    def decode(self, data):
        if len(data) % self.block_size != 0:
            raise ValueError('Length not a multiple of block size')

        last_block = data[-self.block_size:]

        # Get padding amount
        pads = last_block[-1]

        # Validate padding amount
        if pads > self.block_size:
            raise ValueError('Padding amount exceeds block size')

        orig_length = len(data) - pads

        for i in range(self.block_size - 1,
                       (orig_length % self.block_size) - 1,
                       -1):
            if last_block[i] != pads:
                raise ValueError('Inconsistent padding bytes found')

        return data[:-pads]


class BlockCodec(Codec):
    """Break data up into blocks of a given size (no padding at the end by default)"""

    def __init__(self, block_size, right_pad=None):
        self.block_size = block_size

        if right_pad is not None and len(right_pad) != 1:
            raise ValueError('right_pad must be one byte')

        self.right_pad = right_pad

    def encode(self, data):
        step = self.block_size
        blocks = [data[i:i+step] for i in range(0, len(data), step)]

        if self.right_pad is not None and len(blocks[-1]) < self.block_size:
            pad_amount = self.block_size - len(blocks[-1])
            blocks[-1] = blocks[-1] + (self.right_pad * pad_amount)

        return blocks

    def decode(self, data):
        return b''.join(data)
