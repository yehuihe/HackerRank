#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    """Jumping on the Clouds

    Parameters
    ----------
    c : array-like
        An array of binary integers

    Returns
    -------
    jumps : int
        The minimum number of jumps required.
    """
    jumps = 0
    curr = 0
    while curr != len(c)-1:
        curr += 2 if curr+2 <= len(c)-1 and c[curr+2] != 1 else 1
        jumps += 1
    return jumps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print('result: %s' % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
