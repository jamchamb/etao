"""Encoder/decoder classes"""
import base64
import binascii


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


class HexASCIICodec(Codec):

    def __init__(self):
        pass

    def encode(self, data):
        return binascii.hexlify(data)

    def decode(self, data):
        return binascii.unhexlify(data)


class Base64Codec(Codec):

    def __init__(self):
        pass

    def encode(self, data):
        return base64.b64encode(data)

    def decode(self, data):
        return base64.b64decode(data)


class PKCS7PaddingCodec(Codec):

    def __init__(self, block_size):
        self.block_size = block_size

    def encode(self, data):
        pads = self.block_size - (len(data) % self.block_size)
        return data + (chr(pads) * pads)

    def decode(self, data):
        if len(data) % self.block_size != 0:
            raise ValueError('Length not a multiple of block size')

        last_block = data[-self.block_size:]

        # Get padding amount
        pads = ord(last_block[-1])

        # Validate padding amount
        if pads > self.block_size:
            raise ValueError('Padding amount exceeds block size')

        orig_length = len(data) - pads

        for i in range(self.block_size - 1,
                       (orig_length % self.block_size) - 1,
                       -1):
            cur_ord = ord(last_block[i])
            if cur_ord != pads:
                raise ValueError('Inconsistent padding bytes found')

        return data[:-pads]


class BlockCodec(Codec):
    """Break data up into blocks of a given size (no padding at the end)"""

    def __init__(self, block_size):
        self.block_size = block_size

    def encode(self, data):
        step = self.block_size
        blocks = [data[i:i+step] for i in range(0, len(data), step)]

        return blocks

    def decode(self, data):
        return ''.join(data)
