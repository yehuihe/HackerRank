#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def utopianTree(n):
    """Utopian Tree solution

    Parameters
    ----------
    n : int
        The number of growth cycles to simulate.

    Returns
    -------
    height: int
        The height of the tree after the given number of cycles.

    """
    height = 0
    for i in range(n + 1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2
    return height


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print("result: %s" % result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
