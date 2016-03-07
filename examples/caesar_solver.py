#!/usr/bin/env python
# Caesar cipher solver
import argparse
import etao


def main():
    parser = argparse.ArgumentParser(description="Caesar cipher solver")
    parser.add_argument('ciphertext', type=str, help='text to decipher')

    args = parser.parse_args()

    # Get every Caesar shift of the ciphertext
    shifts = map(lambda x: etao.caesar_shift(args.ciphertext, x), range(26))

    # Score each shift according to English character frequency.
    # Get tuples that pair the score with the text.
    scored_shifts = map(lambda x: (etao.score_text(x), x), shifts)

    # Sort by score, descending order
    scored_shifts.sort(reverse=True)

    # Print the top 3 results
    for result in scored_shifts[0:3]:
        print '"%s" (%02d%%)' % (result[1], int(result[0] * 100))

if __name__ == "__main__":
    main()
