#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    """Determine the minimum number of bribes

    Parameters
    ----------
    q : array-like
        The positions of the people after all bribes.

    Notes
    -----
    The algorithm is basically a modified bubble sort.
    Adding count for tracking the chaotic case.

    References
    ----------
    https://en.wikipedia.org/wiki/Bubble_sort
    """
    bribes = 0
    while True:
        swapped = False
        count = 0
        for i in range(len(q) - 1):
            # if this pair is out of order
            if q[i] > q[i + 1]:
                # swap them and remember something changed
                q[i], q[i + 1] = q[i + 1], q[i]
                swapped = True
                bribes += 1
                count += 1
                if count > 2:
                    print("Too chaotic")
                    return
            else:
                count = 0
        if not swapped:
            break
    print(bribes)


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
