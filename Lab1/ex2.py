"""
Author: Saffat Hasan
File Name: ex2

Description:
    For a list of hard-coded books, get the frequencies
    and print the RMSE for the first two and plot the rest
    as a histogram
"""


from frequencyAnalysis import *
import urllib_wrapper
import matplotlib_wrapper as plt
import sys

books_ids = [
    59780,
    59802
]

BOOK_URL = "https://www.gutenberg.org/files/{0}/{0}-0.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Using book IDs: {}".format(sys.argv[1:]))
        books = [BOOK_URL.format(item) for item in sys.argv[1:]]
    else:
        print("No command line arguments specified.")
        print("Using default book set: {}".format(books_ids))
        books = [BOOK_URL.format(item) for item in books_ids]
    frequencies = []
    analyzer = FrequencyAnalysisByLetter()
    for i in range(len(books)):
        file_name = "book_{}.txt".format(i + 1)
        urllib_wrapper.downloadBook(books[i], file_name)
        frequencyDictionary = analyzer.getNormalizedFrequencyDict(file_name)
        frequencies.append(frequencyDictionary)

    if len(frequencies) > 1:
        frequency_values_1 = list(frequencies[0].values())
        frequency_values_2 = list(frequencies[1].values())

        rmse = RMSE(frequency_values_1, frequency_values_2)
        print("The RMSE between the first two books is {:.10f}".format(rmse))

    values = [list(f.values()) for f in frequencies]

    for graphing_function in [plt.bar, plt.hist]:
        graphing_function(values)
        plt.show()
