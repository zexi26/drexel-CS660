"""
Author: Saffat Hasan
File Name: ex3

Description:
    1. Estimate the average size of a book in megabytes
    2. Calculate the number of words in a book
        Calculate the average length of words
"""
from frequencyAnalysis import *
import os
import gutenberg_wrapper
import sys

books = [
    "https://www.gutenberg.org/files/59780/59780-0.txt",
    "https://www.gutenberg.org/files/59802/59802-0.txt",
]


def get_word_analysis(file_name):
    analyzer = FrequencyAnalysisByWord()
    frequencyDictionary = analyzer.getFrequencyDict(file_name)

    total = 0
    count = 0
    for key in frequencyDictionary:
        occurrences = frequencyDictionary[key]
        count += occurrences
        total += len(key) * occurrences

    print("\tTotal words counted: {}".format(count))
    print("\tAverage word length: {0:.2f}".format(total / count))
    return count


def get_file_size(file_name):
    return os.path.getsize(file_name)


if __name__ == "__main__":
    words = []
    sizes = []
    books = gutenberg_wrapper.getBooks(sys.argv[1:])
    for file_name in books:
        print("For file: {}".format(file_name))
        word_count = get_word_analysis(file_name)
        size = get_file_size(file_name)

        print("\tSize of file is {} bytes.\n".format(size))

        sizes.append(size)
        words.append(word_count)
    print("Statistics over all files:")
    print(
        "\tAverage word count over {} books: {}.".format(
            len(books),
            sum(words) /
            len(books)))
    print(
        "\tAverage file size over {} files: {}.".format(
            len(books),
            sum(sizes) /
            len(books)))
