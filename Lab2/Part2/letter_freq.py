import re

from mrjob.job import MRJob

WORD_RE = re.compile("[a-zA-Z]")


class MRLetterFrequency(MRJob):

    def mapper(self, _, line):
        for letter in WORD_RE.findall(line):
            yield letter.lower(), 1

    def combiner(self, letter, counts):
        yield letter, sum(counts)


if __name__ == '__main__':
    MRLetterFrequency.run()
