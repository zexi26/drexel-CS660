#!/usr/bin/python3
import string
import numpy as np


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
