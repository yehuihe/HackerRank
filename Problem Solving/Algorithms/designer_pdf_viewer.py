#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#


def designerPdfViewer(h, word):
    """Designer PDF Viewer solution

    Parameters
    ----------
    h : array-like
        The heights of each letter.

    word : str
        A string.

    Returns
    -------
    result : int
        The size of the highlighted area.
    """
    tallest_height = 0
    for c in word:
        if h[ord(c) - 97] > tallest_height:
            tallest_height = h[ord(c) - 97]
    return tallest_height * len(word)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
