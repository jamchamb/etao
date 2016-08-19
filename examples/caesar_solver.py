#!/usr/bin/env python
# Caesar cipher solver
import argparse
import etao


def main():
    parser = argparse.ArgumentParser(description="Caesar cipher solver")
    parser.add_argument('ciphertext', type=str, help='text to decipher')

    args = parser.parse_args()

    # Get every Caesar shift of the ciphertext
    shifts = [etao.caesar_shift(args.ciphertext, n) for n in range(26)]

    # Score each shift according to English character frequency.
    # Get tuples that pair the score with the text.
    scored_shifts = [(etao.score_text(shift), shift) for shift in shifts]

    # Sort by score, descending order
    scored_shifts.sort(reverse=True)

    # Print the top 3 results
    for result in scored_shifts[0:3]:
        print '"%s" (%02d%%)' % (result[1], int(result[0] * 100))

if __name__ == "__main__":
    main()
