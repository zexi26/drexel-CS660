import re
from collections import defaultdict
from operator import itemgetter

from mrjob.job import MRJob

WORD_RE = re.compile("[\w']+")


class InvertedIndexBaseline(MRJob):

    def mapper(self, _, line):
        document_id, document, h = int(line[:5]), line[5:].lower(), defaultdict(int)

        for term in WORD_RE.findall(document):
            h[term] += 1

        for term, frequency in h.items():
            yield term, (document_id, frequency)

    def reducer(self, term, values):
        postings = [value for value in values]
        postings.sort(key=itemgetter(1), reverse=True)

        yield term, postings


if __name__ == "__main__":
    InvertedIndexBaseline.run()
