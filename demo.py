#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import parla
import codecs

def main():
    result = parla.parse("./assets/quixote.txt")
    with codecs.open("./result.txt", "wb", "utf-8") as f:
        for r in result:
            f.write(u"{0}: {1}\n".format(r[0], r[1]))
    parla.summary(result)

if __name__ == "__main__":
    main()
