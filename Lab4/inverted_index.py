import re
from collections import defaultdict
from operator import itemgetter

from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

WORD_RE = re.compile("[\w']+")


def encode_document(id, text):
    return JSONValueProtocol.write(None, {"id": id, "text": text}) + "\n"


class InvertedIndexBaseline(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, json):
        document_id, document, h = json["id"], json["text"].lower(), defaultdict(int)

        for term in WORD_RE.findall(document):
            h[term] += 1

        for term, frequency in h.items():
            yield term, (document_id, frequency)

    def reducer(self, term, values):
        postings = [value for value in values]
        postings.sort(key=itemgetter(0))

        yield term, postings


class InvertedIndexRevised(MRJob):

    def mapper(self, _, line):
        document_id, document, h = int(line[:5]), line[5:].lower(), defaultdict(int)

        for term in WORD_RE.findall(document):
            h[term] += 1

        for term, frequency in h.items():
            yield (term, document_id), frequency


if __name__ == "__main__":
    InvertedIndexBaseline.run()
    #InvertedIndexRevised.run()
