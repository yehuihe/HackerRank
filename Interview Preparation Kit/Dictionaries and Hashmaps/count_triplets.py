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
    # A O(n^3) brute force solution.
    # triplets = 0
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[j] // r == arr[i]:
    #             for k in range(j+1, len(arr)):
    #                 if arr[k] // r == arr[j]:
    #                     triplets += 1
    # return triplets

    triplets = 0
    # # Construct value counting record
    # record = {}
    # for v in arr:
    #     if v not in record:
    #         record[v] = 0
    #     record[v] += 1

    # Looping over arr and select second number as pivot.
    # Calculate left and right number of pivot
    for i, v in enumerate(arr):
        first = v / r
        third = v * r
        ########
        num_of_first = 0
        for u in arr[:i]:
            if u == first:
                num_of_first += 1
        # if not record.get(first):
        #     num_of_first = 0
        # else:
        #     num_of_first = record.get(first)
        ########
        num_of_third = 0
        for u in arr[i+1:]:
            if u == third:
                num_of_third += 1
        # num_of_first = 0 if not record.get(first) else record.get(first)
        # num_of_third = 0 if not record.get(third) else record.get(third)
        triplets  += num_of_first * num_of_third
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
