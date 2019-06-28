"""
Author: Saffat Hasan
File Name: ex2

Description:
    For a list of hard-coded books, get the frequencies
    and print the RMSE for the first two and plot the rest
    as a histogram
"""


from frequencyAnalysis import getFrequencyDict, RMSE
import urllib_wrapper
import matplotlib_wrapper as plt

books = [
    "https://www.gutenberg.org/files/59780/59780-0.txt",
    "https://www.gutenberg.org/files/59802/59802-0.txt",
]

if __name__ == "__main__":
    frequencies = []

    for i in range(len(books)):
        file_name = "book_{}.txt".format(i + 1)
        urllib_wrapper.downloadBook(books[i], file_name)
        frequencyDictionary = getFrequencyDict(file_name)
        frequencies.append(frequencyDictionary)

    frequency_values_1 = list(frequencies[0].values())
    frequency_values_2 = list(frequencies[1].values())

    rmse = RMSE(frequency_values_1, frequency_values_2)
    print("The RMSE between these two books is {:.10f}".format(rmse))


    values = [list(f.values()) for f in frequencies]
    plt.hist(values)
