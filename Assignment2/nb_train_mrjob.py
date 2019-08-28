import re
from collections import defaultdict

from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol, PickleProtocol

WORD_RE = re.compile(r'\w+')


class NaiveBayesTrainJob(MRJob):
    INPUT_PROTOCOL = JSONProtocol
    OUTPUT_PROTOCOL = JSONProtocol
    SORT_VALUES = True

    def mapper(self, key, email):
        self.increment_counter("calls", "mapper", 1)

        category = int(key.split(",")[0])

        frequencies = {}
        frequencies[0] = defaultdict(int)
        frequencies[1] = defaultdict(int)

        token_count = 0

        for token in WORD_RE.findall(email):
            token_count += 1
            frequencies[category][token] += 1

        # A's will arrive at the reducer first with SORTED_VALUES = True
        yield category, ("A", (1, token_count))

        for category, token_frequencies in frequencies.items():
            for token, frequency in token_frequencies.items():
                yield category, ("B", (token, frequency))

    def reducer(self, category, token_frequencies):
        self.increment_counter("calls", "reducer", 1)

        document_count = 0
        token_count = 0
        frequencies = defaultdict(int)
        for key, values in token_frequencies:
            if key == "A":
                document, token = values
                document_count += document
                token_count += token
            else:
                token, frequency = values
                frequencies[token] += frequency

        training_data = {}
        for token, freq in frequencies.items():
            training_data[token] = (freq, freq / token_count)

        yield "%i_document_count" % category, document_count
        yield "%i_token_count" % category, token_count
        yield "%i_training_data" % category, training_data
        # yield category, list(token_frequencies)


if __name__ == "__main__":
    NaiveBayesTrainJob.run()
