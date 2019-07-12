import requests
import sys

num_copies = sys.argv[1]


def downloadFile(file_name):
    response = requests.get("http://www.gutenberg.org/files/2600/2600-0.txt")
    with open(file_name, 'wb') as f:
        f.write(response.content)


def duplicateFile(source, num_copies):
    destination_file_name = "{}_{}".format(num_copies, source)
    with open(destination_file_name, 'wb') as destination:
        for i in range(num_copies):
            with open(source, 'rb') as source_file:
                for line in source_file:
                    destination.write(line)


if __name__ == "__main__":
    num_copies = sys.argv[1]
    downloadFile("sampleBook.txt")
    duplicateFile("sampleBook.txt", num_copies)
