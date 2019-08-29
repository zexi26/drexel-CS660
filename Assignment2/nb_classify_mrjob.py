import json
import re
from collections import defaultdict

import numpy as np
from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol

WORD_RE = re.compile(r'\w+')


class NaiveBayesClassifier(MRJob):
    INPUT_PROTOCOL = JSONProtocol
    OUTPUT_PROTOCOL = JSONProtocol

    def configure_args(self):
        super(NaiveBayesClassifier, self).configure_args()
        self.add_file_arg("--training_data")

    def mapper(self, key, email):
        self.increment_counter("calls", "mapper", 1)

        freqs = defaultdict(int)

        for token in WORD_RE.findall(email):
            freqs[token] += 1

        key = int(key.split(",")[1])
        for token, freq in freqs.items():
            yield key, (token, freq)

    def reducer_init(self):
        self.increment_counter("calls", "reducer_init", 1)

        training_data = {}

        for line in open(self.options.training_data, "r"):
            k_str, v_str = line.split("\t", 1)

            training_data[json.loads(k_str)] = json.loads(v_str)

        # word frequency dicts
        self.spam_dict = training_data["1_training_data"]
        self.ham_dict = training_data["0_training_data"]

        spam_vocab = list(self.spam_dict.keys())
        ham_vocab = list(self.ham_dict.keys())
        vocab = set().union(*[spam_vocab, ham_vocab])
        self.vocab_size = len(vocab)

        # document counts
        spam_d_count = training_data["1_document_count"]
        ham_d_count = training_data["0_document_count"]
        total_d_count = spam_d_count + ham_d_count

        # token counts
        self.spam_t_count = training_data["1_token_count"]
        self.ham_t_count = training_data["0_token_count"]

        # prior probabilities
        self.spam_prior = spam_d_count / total_d_count
        self.ham_prior = ham_d_count / total_d_count

    def reducer(self, key, values):
        self.increment_counter("calls", "reducer", 1)

        tokens = list(values)
        p_spam = 0
        p_ham = 0

        for token, freq in tokens:
            ps_denom = self.spam_t_count + self.vocab_size + 1
            ph_denom = self.ham_t_count + self.vocab_size + 1

            ps = (self.spam_dict.get(token, (1, 1 / ps_denom))[0] + 1) / ps_denom
            ph = (self.ham_dict.get(token, (1, 1 / ph_denom))[0] + 1) / ph_denom

            p_spam += (-np.log10(ps) * freq)
            p_ham += (-np.log10(ph) * freq)

        spam_prior = -np.log10(self.spam_prior)
        ham_prior = -np.log10(self.ham_prior)

        yield (str(key)), (1 if (spam_prior + p_spam) < (ham_prior + p_ham) else 0)


if __name__ == "__main__":
    NaiveBayesClassifier.run()
