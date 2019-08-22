import re
from collections import defaultdict

from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol

WORD_RE = re.compile(r'\w+')

class NaiveBayesJob(MRJob):
    INPUT_PROTOCOL = JSONProtocol

    def mapper(self, category, email):

        total_count = 0
        frequencies = {}
        frequencies[0] = defaultdict(int)
        frequencies[1] = defaultdict(int)

        for token in WORD_RE.findall(email):
            total_count += 1
            frequencies[category][token] += 1

        for category, word_frequencies in frequencies.items():
            for word, frequency in word_frequencies.items():
                yield category, (word, frequency)

    def reducer(self, category, word_frequencies):
        yield category, list(word_frequencies)


if __name__ == "__main__":
    NaiveBayesJob.run()
