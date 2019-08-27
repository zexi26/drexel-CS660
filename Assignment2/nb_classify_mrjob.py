import hashlib
import json
import re
from collections import defaultdict

import numpy as np
from mrjob.job import MRJob

WORD_RE = re.compile(r'\w+')


class NaiveBayesClassifier(MRJob):

    def configure_args(self):
        super(NaiveBayesClassifier, self).configure_args()
        self.add_file_arg("--training_data")

    def mapper(self, _, email):
        self.increment_counter("calls", "mapper", 1)

        freqs = defaultdict(int)

        for token in WORD_RE.findall(email):
            freqs[token] += 1

        key = hashlib.sha224(email.encode("utf-8")).hexdigest()
        for token, freq in freqs.items():
            yield key, (token, freq)

    def reducer_init(self):
        self.increment_counter("calls", "reducer_init", 1)

        training_data = {}

        for line in open(self.options.training_data, "r"):
            k_str, v_str = line.split("\t", 1)

            training_data[json.loads(k_str)] = json.loads(v_str)

        # word frequency dicts
        self.spam_dict = training_data["1"]
        self.ham_dict = training_data["0"]

        # document counts
        spam_d_count = training_data["1_count"]
        ham_d_count = training_data["0_count"]
        total_d_count = spam_d_count + ham_d_count

        # token counts
        self.spam_t_count = sum(self.spam_dict.values())
        self.ham_t_count = sum(self.ham_dict.values())

        # prior probabilities
        self.spam_prior = spam_d_count / total_d_count
        self.ham_prior = ham_d_count / total_d_count

    def reducer(self, key, values):
        self.increment_counter("calls", "reducer", 1)

        tokens = list(values)
        p_spam = np.prod([((self.spam_dict.get(token, 0) + 1) / self.spam_t_count) ** freq for token, freq in tokens])
        p_ham = np.prod([((self.ham_dict.get(token, 0) + 1) / self.ham_t_count) ** freq for token, freq in tokens])

        yield key, (1 if (self.spam_prior * p_spam) > (self.ham_prior * p_ham) else 0)


if __name__ == "__main__":
    NaiveBayesClassifier.run()
