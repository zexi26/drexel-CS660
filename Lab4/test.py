from mrjob.job import MRJob
import re
import csv
from mrjob.step import MRStep
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
            count[(key, value)] += 1
        for k, v in count.items():
            yield None, (k, v)

    # def reducer_list(self, _, pairs):
        # postings = defaultdict()
        # for pair in pairs:
            # postings[pair[0]].append(pair[1], count)

        # for (k, v) in postings.items():
        #     yield k, v

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_count),
            # MRStep(reducer=self.reducer_list)

        ]


if __name__ == '__main__':
    MRInvertedIndex.run()