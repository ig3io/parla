# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import codecs
import operator


def parse(path):
    if not os.path.exists(path):
        raise IOError("Cannot access the file {0}".format(path))

    words = {}
    # This allows us to read line by line without buffering the
    # entire file
    with codecs.open(path, "r", "utf-8-sig", "utf-8") as f:
        for line in f:
            for w in line.split():
                w = w.strip()  # Remove whitespace
                w = w.strip(",.:;-'\"?¿!¡»«")
                w = w.lower()
                words[w] = words.get(w, 0) + 1
    return _interpret(words)


def _interpret(words_dict):
     words = sorted(words_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
     return words
