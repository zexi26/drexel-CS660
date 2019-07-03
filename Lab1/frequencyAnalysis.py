#!/usr/bin/python3
import string
import numpy as np


class FrequencyAnalysis:
    """ Base class for Frequency Analysis """

    def __init__(self):
        self.frequencyDictionary = None

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


def getFrequencyDict(file_name):
    """ Returns a dictionary of each letter and its frequency """
    freq = {}
    count = 0
    for c in string.ascii_lowercase:
        freq[c] = 0

    for line in open(file_name, encoding="utf8"):
        for c in line.lower():
            if c not in freq:
                continue
            freq[c] += 1
            count += 1
    for key in freq:
        freq[key] /= count
    return freq


def getFrequencyWordDict(file_name):
    freq = {}

    for line in open(file_name, encoding="utf8"):
        for word in line.lower().split():
            if not word:
                continue
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

    return freq


def RMSE(list1, list2):
    """ calculate root mean square error by summing the
    squares of each difference and returning the square root """
    return np.sqrt(((np.array(list1) - np.array(list2)) ** 2).mean())
