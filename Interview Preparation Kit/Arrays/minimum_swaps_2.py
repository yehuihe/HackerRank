#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    """Minimumm swaps for unordered array

    Parameters
    ----------
    arr : array-like
        An unordered array of integers.

    Returns
    -------
    min_swaps : int
        The minimum number of swaps to sort the array.

    Notes
    -----
    The algorithm is basically a modified selection sort.
    Adding count for tracking swaps.

    This solution will have a timeout issue on HackerRank
    due to selection sort's O(n^2) complexity. It wouldn't give
    you full points.

    I saw other people's solution use the fact that there are no
    duplicates and consecutive integers cut complexity to O(nlogn).
    That will work for HackerRank.

    References
    ----------
    https://en.wikipedia.org/wiki/Selection_sort
    """
    swaps = 0
    for i in range(len(arr) - 1):
        # Find the min element in the unsorted arr[0, len(arr)-1]

        # Assume the min is the first element
        min = i
        # Test against elements after i to find the smallest
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            swaps += 1
    return swaps


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print("result: %s" % res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
