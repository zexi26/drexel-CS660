from mrjob.job import MRJob
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
        count = defaultdict(int)
        for value in values:
            count[value] += 1
            
        postings = []
        for k, v in count.items():
            postings.append((k, v))
        
        yield key, postings


    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_count)
        ]


if __name__ == '__main__':
    MRInvertedIndex.run()
