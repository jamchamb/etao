"""Scorer classes"""
from .analysis import ngram_frequency, cosine_similarity
from .freq import ENGLISH_FREQ


class NgramFrequencyScorer:
    """Score how well a text matches a given frequency table.
    Case insensitive. Uses English letter frequency by default.
    Only characters with an entry in the frequency table are considered.
    The result is the cosine similarity of the frequency tables of the text
    and the language, where a value of 1 indicates most similar and
    a value of 0 indicates least similar."""

    def __init__(self, freq=ENGLISH_FREQ):

        if len(freq) == 0:
            raise ValueError("Empty frequency table")

        # Determine ngram length and ensure it's conistent throughout the table
        ngram_length = len(freq.keys()[0])

        for k in freq.keys():
            if k != k.lower():
                raise ValueError("Only use lower-case keys in frequency table")
            elif len(k) != ngram_length:
                raise ValueError("All frequency table keys should have the " +
                                 "same length")

        self.freq = freq
        self.ngram_length = ngram_length

    def score(self, text):
        if len(text) == 0:
            return 0

        text_freq = ngram_frequency(text, self.ngram_length)

        # Get vector for each frequency table
        freq_vector = []
        text_vector = []

        for key in self.freq.keys():
            freq_vector.append(self.freq[key])
            text_vector.append(text_freq.get(key) or 0.0)

        return cosine_similarity(text_vector, freq_vector)
