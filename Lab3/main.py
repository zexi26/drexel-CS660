import sys

import requests


def download_file(file_name):
    response = requests.get("http://www.gutenberg.org/files/2600/2600-0.txt")
    with open(file_name, 'wb') as f:
        f.write(response.content)


def duplicate_file(source, num_copies):
    destination_file_name = "{}_{}".format(num_copies, source)

    with open(source, 'r') as in_file, open(destination_file_name, 'w') as out_file:
        big_string = ""
        text = in_file.read()
        for i in range(num_copies):
            big_string += text

        out_file.write(big_string)


if __name__ == "__main__":
    num_copies = int(sys.argv[1])
    download_file("sampleBook.txt")
    duplicate_file("sampleBook.txt", num_copies)
