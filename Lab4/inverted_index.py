import os
import re
from collections import defaultdict, OrderedDict

from mrjob.job import MRJob

WORD_RE = re.compile("[\w']+")


class InvertedIndexRaw(MRJob):
    SORT_VALUES = True

    def mapper_raw(self, input_path, input_uri):
        """Mapper function

        Args:
            input_path (str): a local path that the input file has been copied to
            input_uri (str): the URI of the input file on HDFS, S3, etc

        Yields:
           str, (str, int): a term paired with a tuple containing the ``document_id`` and term frequency

        """
        self.increment_counter("mapper", "calls", 1)

        document_id, h = os.path.basename(input_path).split(".")[0], defaultdict(int)

        with open(input_path, "r") as file:
            for term in WORD_RE.findall(file.read()):
                h[term] += 1

            for term, frequency in h.items():
                yield term, (document_id, frequency)

    def reducer(self, term, values):
        """Reducer function

        Args:
            term (str): a term
            values (generator): a list of tuples from the mapper

        Yields:
            str, list: a term paired with a list of postings (doc_id, tf)

        """
        self.increment_counter("reducer", "calls", 1)

        yield term, [value for value in values]


class InvertedIndexBaseline(MRJob):
    """This job will run the baseline inverted index algorithm from section 4.3"""

    def mapper_init(self):
        """Retrieves ``document_id`` from input file name"""
        self.document_id = int(os.path.basename(os.environ["map_input_file"]).split(".")[0])

    def mapper(self, _, line):
        """Mapper function

        Args:
            _ (None): ignored
            line (str): a line of text from the input

        Yields:
           str, (str, int): a term paired with a tuple containing the ``document_id`` and term frequency

        """
        self.increment_counter("mapper", "calls", 1)

        h = defaultdict(int)

        for term in WORD_RE.findall(line):
            h[term] += 1

        for term, frequency in h.items():
            yield term, (self.document_id, frequency)

    def reducer(self, term, values):
        """Reducer function

        Args:
            term (str): a term
            values (generator): a list of tuples from the mapper

        Yields:
            str, OrderedDict: a term paired with an ``OrderedDict`` of postings (doc_id, tf)

        """
        self.increment_counter("reducer", "calls", 1)

        postings = defaultdict(int)

        for document_id, frequency in values:
            postings[document_id] += frequency

        postings = OrderedDict(sorted(postings.items()))

        yield term, postings


class InvertedIndexRevised(MRJob):
    """This job will run the revised inverted index algorithm from section 4.4"""

    SORT_VALUES = True

    def mapper_init(self):
        """Retrieves ``document_id`` from input file name"""
        self.document_id = os.path.basename(os.environ["map_input_file"]).split(".")[0]

    def mapper(self, _, line):
        """Mapper function

        Args:
            _ (None): ignored
            line (str): a line of text from the input

        Yields:
           str, (str, int): a term paired with a tuple containing the ``document_id`` and term frequency

        """
        self.increment_counter("mapper", "calls", 1)

        h = defaultdict(int)

        for term in WORD_RE.findall(line):
            h[term] += 1

        for term, frequency in h.items():
            yield term, (self.document_id, frequency)

    def reducer(self, term, values):
        """Reducer function

        Args:
            term (str): a term
            values (generator): a list of tuples from the mapper

        Yields:
            str, defaultdict: a term paired with a ``defaultdict`` of postings (doc_id, tf)

        """
        self.increment_counter("reducer", "calls", 1)

        postings = defaultdict(int)

        for document_id, frequency in values:
            postings[document_id] += frequency

        # No need to sort!

        yield term, postings


if __name__ == "__main__":
    # InvertedIndexBaseline.run()
    # InvertedIndexRevised.run()
    InvertedIndexRaw.run()
