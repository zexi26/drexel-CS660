import csv
import re
from collections import defaultdict

from mrjob.job import MRJob

WORD_RE = re.compile("[\w']+")


class MRInvertedIndex(MRJob):

    def mapper(self, _, value):
        for row in (csv.reader([value])):
            doc_id = row[0]
            for word in WORD_RE.findall(row[1].lower()):
                yield word, doc_id

    def reducer(self, key, values):
        """ Given a term and a list document IDs
            yield the term with a list of [ (doc_id, occurrences), ... ] """
        count = defaultdict(int)

        for document_id in values:
            count[document_id] += 1

        postings = []
        for document_id, occurrences in count.items():
            postings.append((document_id, occurrences))

        yield key, postings


if __name__ == '__main__':
    MRInvertedIndex.run()
