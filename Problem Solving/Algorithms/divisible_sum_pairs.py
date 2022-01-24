#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    """Divisible Sum Pairs solutions

    Parameters
    ----------
    n : int
        The length of array ar.

    k : int
        The integer divisor.

    ar : array-like
        An array of integers.

    Returns
    -------
    res: int
        The number of pairs.
    """
    res = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                res += 1
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print('result: %s' % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
