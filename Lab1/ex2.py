"""
Author: Saffat Hasan
File Name: ex2

Description:
    For a list of hard-coded books, get the frequencies
    and print the RMSE for the first two and plot the rest
    as a histogram
"""


from frequencyAnalysis import *
import matplotlib_wrapper as plt
import sys
import gutenberg_wrapper

books_ids = [
    59780,
    59802
]

BOOK_URL = "https://www.gutenberg.org/files/{0}/{0}-0.txt"


def printRMSE(frequencies):
    if len(frequencies) <= 1:
        return
    frequency_values_1 = list(x[1] for x in frequencies[0])
    frequency_values_2 = list(x[1] for x in frequencies[1])

    rmse = RMSE(frequency_values_1, frequency_values_2)
    print("The RMSE between the first two books is {:.10f}".format(rmse))


if __name__ == "__main__":
    # If specified, use command line arguments
    # getBooks has a default if the array contains nothing
    books = gutenberg_wrapper.getBooks(sys.argv[1:])
    frequencies = []
    analyzer = FrequencyAnalysisByLetter()

    for file_name in books:
        frequencyDictionary = analyzer.getNormalizedFrequencyDict(file_name)
        frequencies.append(frequencyDictionary)

    printRMSE(frequencies)

    values = [[x[1] for x in f] for f in frequencies]

    for graphing_function in [plt.bar, plt.hist]:
        graphing_function(values)
        plt.show()
