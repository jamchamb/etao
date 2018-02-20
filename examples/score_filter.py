#!/usr/bin/env python
# Filter text by ngram score from stdin
import argparse
import fileinput
from etao import NgramFrequencyScorer
from etao.freq import ENGLISH_DIGRAMS


def main():
    parser = argparse.ArgumentParser(description="ngram score filter")
    parser.add_argument('--cutoff', type=float, default=0.25)
    parser.add_argument('rest', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    scorer = NgramFrequencyScorer(freq=ENGLISH_DIGRAMS)

    for line in fileinput.input(args.rest):
        score = scorer.score(line)
        if score > args.cutoff:
            print line


if __name__ == "__main__":
    main()
