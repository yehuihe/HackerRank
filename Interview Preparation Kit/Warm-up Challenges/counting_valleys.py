#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    """Counting valleys

    Given the sequence of up and down steps during a hike,
     find and print the number of valleys walked through.

    Parameters
    ----------
    steps : int
        The number of steps on the hike.
    path : str
        A string describing the path.

    Returns
    -------
    valleys: int
        The number of valleys traversed.
    """
    valleys = 0
    level = 0
    is_valley = False
    for p in path:
        level = level + 1 if p == "U" else level - 1
        if level == -1 and not is_valley:
            is_valley = True
        if is_valley and level == 0:
            valleys += 1
        if level == 0:
            is_valley = False
    return valleys


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
