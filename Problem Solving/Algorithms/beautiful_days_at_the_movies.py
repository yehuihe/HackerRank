#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


def beautifulDays(i, j, k):
    """Beautiful Days solutions

    Parameters
    ----------
    i : int
        the starting day number.

    j : int
        The ending day number.

    k : int
        The divisor.

    Returns
    -------
    days : int
        The number of beautiful days in the range.
    """
    days = 0
    for v in range(i, j + 1):
        rev = int(str(v)[::-1])
        if abs(v - rev) % k == 0:
            days += 1
    return days


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
