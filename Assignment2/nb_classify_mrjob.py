import json
import re

from mrjob.job import MRJob

WORD_RE = re.compile(r'\w+')


class NaiveBayesClassifier(MRJob):

    def configure_args(self):
        super(NaiveBayesClassifier, self).configure_args()
        self.add_file_arg("--training_data")

    def mapper_init(self):
        training_data = {}

        for line in open(self.options.training_data, "r"):
            k_str, v_str = line.split("\t", 1)

            training_data[json.loads(k_str)] = json.loads(v_str)

        ### this stuff may be moved to reducer, not sure

        # document counts
        spam_d_count = training_data["1_total"]
        ham_d_count = training_data["0_total"]
        total_d_count = spam_d_count + ham_d_count

        # prior probabilities
        self.spam_prior = spam_d_count / total_d_count
        self.ham_prior = ham_d_count / total_d_count

        # word frequency dicts
        self.spam_dict = training_data["1"]
        self.ham_dict = training_data["0"]

    def mapper(self, _, email):
        for token in WORD_RE.findall(email):

            # add 1 smoothing
            spam_count = self.spam_dict.get(token, 0) + 1
            ham_count = self.ham_dict.get(token, 0) + 1

            yield 1, token


if __name__ == "__main__":
    NaiveBayesClassifier.run()
