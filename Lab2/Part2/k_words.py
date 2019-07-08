import re

from mrjob.job import MRJob
from mrjob.step import MRStep

WORD_RE = re.compile(r"[\w']+")


class MRWordSort(MRJob):

    def configure_args(self):
        super(MRWordSort, self).configure_args()

        self.add_passthru_arg("--k", type=int, default=10, help="Number of words to retrieve")

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield None, (sum(counts), word)

    def reducer_sort(self, _, pairs):
        pairs = sorted(list(pairs))

        k = self.options.k
        size = len(pairs)

        if k > size:
            k = size

        for _ in range(0, k):
            yield pairs.pop()

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_sort)
        ]


if __name__ == '__main__':
    # Usage:
    #   python3 k_words.py input.txt --k=5
    MRWordSort.run()
