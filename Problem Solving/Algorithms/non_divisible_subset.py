#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


# TODO: Stuck
def nonDivisibleSubset(k, s):
    """Non-Divisible Subset solution

    Parameters
    ----------
    k : int
        The divisor.

    s : array-like
        An array of integers.

    Returns
    -------
    maximal_subset : int
        The length of the longest subset of S meeting the criteria.
    """
    from itertools import combinations

    record = set()
    for t in combinations(s, 2):
        if sum(t) % k != 0:
            for v in t:
                record.add(v)

    # res = 0
    # for r in reversed(range(2, len(record))):
    #     print(r)
    #     for t in combinations(record, r):
    #         print(t)
    #         stop = True
    #         for v in combinations(t, 2):
    #             if sum(v) % k == 0:
    #
    pass


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print("result: %s" % result)

    # fptr.write(str(result) + "\n")

    # fptr.close()
