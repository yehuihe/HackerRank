#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    """Picking Number solution

    Parameters
    ----------
    a : array-like
        An array of integers.

    Returns
    -------
    res : int
        The length of the longest subarray that meets the criterion.
    """
    res = 0
    for i in a:
        b = a.count(i)
        s = a.count(i - 1)
        if b + s > res:
            res = b + s
    return res


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print("result: %s" % result)

    # fptr.write(str(result) + "\n")

    # fptr.close()
