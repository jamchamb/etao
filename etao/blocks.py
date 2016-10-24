"""Block crypto"""


def get_blocks(data, block_size):
    """Return input buffer broken up into blocks of given size."""

    # Break buffer up into blocks
    blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]

    return blocks
