#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import parla
import codecs
import matplotlib.pyplot as plt


def main():
    p = parla.Zipf("./assets/quixote.txt")
    with codecs.open("./result.txt", "wb", "utf-8") as f:
        for r in p.words:
            f.write(u"{0}: {1}\n".format(r[0], r[1]))
    p.summary()
    p.plot()
    #p.show()
    p.save("result.png")

if __name__ == "__main__":
    main()
