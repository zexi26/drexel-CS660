import re
from collections import defaultdict

from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol, PickleProtocol

WORD_RE = re.compile(r'\w+')


class NaiveBayesTrainJob(MRJob):
    INPUT_PROTOCOL = JSONProtocol
    OUTPUT_PROTOCOL = JSONProtocol
    SORT_VALUES = True

    def mapper(self, category, email):
        self.increment_counter("calls", "mapper", 1)

        total_count = 0
        frequencies = {}
        frequencies[0] = defaultdict(int)
        frequencies[1] = defaultdict(int)

        for token in WORD_RE.findall(email):
            total_count += 1
            frequencies[category][token] += 1

        # A's will arrive at the reducer first with SORTED_VALUES = True
        yield category, ("A", total_count)

        for category, token_frequencies in frequencies.items():
            for token, frequency in token_frequencies.items():
                yield category, ("B", (token, frequency))

    def reducer(self, category, token_frequencies):
        self.increment_counter("calls", "reducer", 1)

        total = 0
        frequencies = defaultdict(int)
        for key, values in token_frequencies:
            if key == "A":
                total += values
            else:
                token, frequency = values
                frequencies[token] += frequency

        yield category, total
        yield category, frequencies
        # yield category, list(token_frequencies)


if __name__ == "__main__":
    NaiveBayesTrainJob.run()
