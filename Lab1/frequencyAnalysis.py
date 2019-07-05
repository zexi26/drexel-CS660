#!/usr/bin/python3
import string
import numpy as np


class FrequencyAnalysis:
    """ Base class for Frequency Analysis """

    def getFrequencyDict(self, file_name):
        self.frequencyDictionary = {}

        for line in open(file_name, encoding="utf8"):
            for token in self.parseLine(line):
                if token not in self.frequencyDictionary:
                    self.frequencyDictionary[token] = 1
                else:
                    self.frequencyDictionary[token] += 1

        self.filterDictionary()
        return self.frequencyDictionary

    def getNormalizedFrequencyDict(self, file_name):
        freq = self.getFrequencyDict(file_name)
        total_occurrences = sum(freq[key] for key in freq)

        for key in freq:
            freq[key] /= total_occurrences

        freq = sorted(freq.items(), key=lambda x: x[0])
        return freq

    def parseLine(self, line):
        raise NotImplemented

    def filterDictionary(self):
        raise NotImplemented


class FrequencyAnalysisByLetter(FrequencyAnalysis):
    def parseLine(self, line):
        """ Splits word by character """
        line.lower()
        return line

    def filterDictionary(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        keys = list(self.frequencyDictionary.keys())
        for key in keys:
            if key not in alphabet:
                self.frequencyDictionary.pop(key)


class FrequencyAnalysisByWord(FrequencyAnalysis):
    def parseLine(self, line):
        """ Splits words by whitespace """
        line.lower()
        return line.split()

    def filterDictionary(self):
        """ We do not filter any keys out of the dictionary in this class """
        pass


def RMSE(list1, list2):
    """ calculate root mean square error by summing the
    squares of each difference and returning the square root """
    return np.sqrt(((np.array(list1) - np.array(list2)) ** 2).mean())
