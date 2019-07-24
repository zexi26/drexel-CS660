import os
import re
from collections import defaultdict, OrderedDict

from mrjob.job import MRJob

WORD_RE = re.compile("[\w']+")


class InvertedIndexBaseline(MRJob):

    def mapper_init(self):
        self.document_id = int(os.path.basename(os.environ["map_input_file"]).split(".")[0])

    def mapper(self, _, json):
        self.increment_counter("mapper", "calls", 1)

        document, document_id, h = json, self.document_id, defaultdict(int)

        for term in WORD_RE.findall(document):
            h[term] += 1

        for term, frequency in h.items():
            yield term, (document_id, frequency)

    def reducer(self, term, values):
        self.increment_counter("reducer", "calls", 1)

        postings = defaultdict(int)

        for document_id, frequency in values:
            postings[document_id] += frequency

        postings = OrderedDict(sorted(postings.items()))

        yield term, postings


class InvertedIndexRevised(MRJob):
    SORT_VALUES = True

    def mapper_init(self):
        self.document_id = int(os.path.basename(os.environ["map_input_file"]).split(".")[0])

    def mapper(self, _, json):
        self.increment_counter("mapper", "calls", 1)

        document, document_id, h = json, self.document_id, defaultdict(int)

        for term in WORD_RE.findall(document):
            h[term] += 1

        for term, frequency in h.items():
            yield term, (document_id, frequency)

    def reducer(self, term, values):
        self.increment_counter("reducer", "calls", 1)

        postings = defaultdict(int)

        for document_id, frequency in values:
            postings[document_id] += frequency

        # No need to sort!

        yield term, postings


if __name__ == "__main__":
    # InvertedIndexBaseline.run()
    InvertedIndexRevised.run()
