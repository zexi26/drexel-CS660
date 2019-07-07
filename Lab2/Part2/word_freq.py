import re

from mrjob.job import MRJob

LETTER_RE = re.compile("[^a-zA-Z]")


class MRWordFrequency(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            word = re.sub(LETTER_RE, "", word)
            yield word.lower(), 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordFrequency.run()
