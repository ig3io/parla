# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import codecs
import operator
import matplotlib.pyplot as plt


class Zipf(object):

    def __init__(self, path):
        self.words = []
        self.path = path
        self.words = Zipf.parse(self.path)

    @staticmethod
    def parse(path):
        trim_string = ",.:;-'\"?¿!¡»«"
        if not os.path.exists(path):
            raise IOError("Cannot access the file {0}".format(path))

        words = {}
        # This allows us to read line by line without buffering the
        # entire file
        with codecs.open(path, "r", "utf-8-sig", "utf-8") as f:
            for line in f:
                for w in line.split():
                    w = w.strip()  # Remove whitespace
                    w = w.strip(trim_string)  # Extra chars to trim
                    w = w.lower()  # Case insensitive
                words[w] = words.get(w, 0) + 1
        return sorted(words.iteritems(),
                      key=operator.itemgetter(1),
                      reverse=True)

    @staticmethod
    def words_needed(words, percent, total_words):
        num_words = 0
        partial = 0.0
        for w in words:
            partial += 100.0*float(w[1])/float(total_words)
            num_words += 1
            if partial > percent:
                break
        return num_words

    def summary(self):
        total_words = sum(r[1] for r in self.words)
        total_unique_words = len(self.words)
        print("Number of words: {0}".format(total_words))
        print("Number of unique words: {0}".format(total_unique_words))
        print("Top ten:")
        for i in range(10):
            w = self.words[i]
            print("{0} - {1} - {2} - {3}%".format(i, w[0], w[1], 100.0*float(w[1])/float(total_words)))
        print("\nNumber of words needed to understand 50% of the text: {0}".format(Zipf.words_needed(self.words, 50.0, total_words)))
        print("\nNumber of words needed to understand 60% of the text: {0}".format(Zipf.words_needed(self.words, 60.0, total_words)))
        print("\nNumber of words needed to understand 80% of the text: {0}".format(Zipf.words_needed(self.words, 80.0, total_words)))
    

    def plot(self):
        x = range(100)
        y = [word[1] for word in self.words[:100]]
        plt.xkcd()
        plt.plot(x, y)

    def show(self):
        plt.show()

    def save(self, path):
        plt.savefig(path)
