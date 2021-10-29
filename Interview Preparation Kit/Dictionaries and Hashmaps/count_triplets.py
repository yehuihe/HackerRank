#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    """Count Triplets in an array

    Parameters
    ----------
    arr : array-like
        An array of integers.
    r : int
        The common ratio.

    Returns
    -------
    triplets : int
        The number of triplets.
    """
    triplets = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] // r == arr[i]:
                for k in range(j+1, len(arr)):
                    if arr[k] // r == arr[j]:
                        triplets += 1
    return triplets


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print('result: %s' % ans)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
