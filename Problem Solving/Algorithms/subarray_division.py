#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    """Subarray Division solution

    Parameters
    ----------
    s : array-like
        The numbers on each of the squares of chocolate.

    d : int
        Ron's birth day.

    m : int
        Ron's birth month.

    Returns
    -------
    result : int
        The number of ways the bar can be divided.
    """
    res = 0
    for i in range(len(s) - m + 1):
        if sum(s[i : i + m]) == d:
            res += 1
    return res


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
