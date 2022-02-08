#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    """Forming a Magic Square solution

    Parameters
    ----------
    s : array-like
        A 3 * 3 array of integers.

    Returns
    -------
    min_cost : int
        The minimal total cost of converting the input square to a magic square.
    """


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
