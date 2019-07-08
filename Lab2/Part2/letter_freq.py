import re

from mrjob.job import MRJob
from mrjob.step import MRStep

LETTER_RE = re.compile("[a-zA-Z]")


class MRLetterFrequency(MRJob):

    def mapper(self, _, line):
        for letter in LETTER_RE.findall(line):
            yield letter.lower(), 1

    def combiner(self, letter, counts):
        yield letter, sum(counts)

    def reducer(self, letter, counts):
        yield None, (sum(counts), letter)

    def reducer_freq(self, _, pairs):
        pairs = sorted(list(pairs))

        total = sum([pair[0] for pair in pairs])

        for pair in reversed(pairs):
            yield (pair, pair[0] / total)

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_freq)
        ]


if __name__ == '__main__':
    MRLetterFrequency.run()
