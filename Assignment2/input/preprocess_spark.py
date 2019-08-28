import csv
import hashlib
import re
import sys

WORD_RE = re.compile(r'\w+')

if __name__ == "__main__":
    filename = sys.argv[1]

    print("Pre-processing %s..." % filename)

    with open("./spark_input.txt", "w", encoding="utf-8") as output_file, open(filename, encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file)

        count = 0

        for row in csv_reader:
            count += 1
            # skip that first line
            if count == 1:
                continue

            email = " ".join(WORD_RE.findall(row[1]))

            line = '%i\t"%s"\n' % (0 if row[0] == "ham" else 1, email)

            output_file.write(line)
