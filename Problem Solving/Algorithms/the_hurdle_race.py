#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#


def hurdleRace(k, height):
    """The hurdle race solution

    Parameters
    ----------
    k : int
        The height the character can jump naturally.

    height : array-like
        The heights of each hurdle.

    Returns
    -------
    result : int
        The minimum number of doses required, always 0 or more.
    """
    return max(height) - k if max(height) - k >= 0 else 0


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
