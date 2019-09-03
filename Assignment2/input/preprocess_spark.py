import os
import random
import re

WORD_RE = re.compile(r'\w+')

if __name__ == "__main__":
    with open("./enron_spark_input.txt", "w") as training_file:
        spam_dir = "./enron_full/spam/"
        ham_dir = "./enron_full/ham/"

        training_percent = 0.8

        spam_files = os.listdir(spam_dir)
        ham_files = os.listdir(ham_dir)

        total_spam = len(spam_files)
        total_ham = len(ham_files)

        spam_samples = int(training_percent * total_spam)
        ham_samples = int(training_percent * total_ham)

        count = 1
        spam_count = 1
        for spam_file in spam_files:
            with open("%s%s" % (spam_dir, spam_file), "r", errors="ignore") as f:
                spam = " ".join(WORD_RE.findall(f.read()))

                line = '%i\t"%s"\n' % (1, spam)

                training_file.write(line)

                spam_count += 1
                count += 1

        print("spam_count = ", spam_count)
        print("total_count=", count)
        print()

        ham_count = 1
        for ham_fie in ham_files:
            with open("%s%s" % (ham_dir, ham_fie), "r", errors="ignore") as f:
                ham = " ".join(WORD_RE.findall(f.read()))

                line = '%i\t"%s"\n' % (0, ham)

                training_file.write(line)

                count += 1
                ham_count += 1

        print("spam_count = ", spam_count)
        print("ham_count = ", ham_count)
        print("spam + ham = ", spam_count + ham_count)
        print("total_count=", count)
        print()