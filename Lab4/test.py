from mrjob.job import MRJob, MRStep
import re
import csv
from collections import defaultdict

WORD_RE = re.compile("[\w']+")


class MRInvertedIndex(MRJob):

    def mapper(self, _, value):
        for row in (csv.reader([value])):
            doc_id = row[0]
            for word in WORD_RE.findall(row[1].lower()):
                yield word, doc_id

    def reducer_count(self, key, values):
        """ Given a term and a list document IDs
            yield the term with a list of [ (doc_id, occurrences), ... ] """
        count = defaultdict(int)

        for document_id in values:
            count[document_id] += 1

        postings = []
        for document_id, occurrences in count.items():
            postings.append((document_id, occurrences))

        yield key, postings


    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_count)
        ]


if __name__ == '__main__':
    MRInvertedIndex.run()
