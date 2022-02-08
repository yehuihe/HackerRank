#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def arrayManipulation(n, queries):
    """Array Manippulation

    Parameters
    ----------
    n : int
        The number of elements in your array.

    queries : array-like
        A two dimensional array of queries where each queries[i]
        contains three integers, a, b, and k.

    Notes
    -----
    O(n^2) complexity. Not for HackerRank. I'm working on it.

    Returns
    -------
    max_v : int
        Return the integer maximum value in the finished array.
    """
    temp = [0] * n
    for query in queries:
        a = query[0] - 1
        b = query[1] - 1
        k = query[2]
        for i in range(a, b + 1):
            temp[i] += k
    return max(temp)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
