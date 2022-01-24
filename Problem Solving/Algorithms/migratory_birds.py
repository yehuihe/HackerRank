#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    """Migratory Birds solution

    Parameters
    ----------
    arr : array-like
        The types of birds sighted.

    Returns
    -------
    res: int
        The lowest type id of the most frequently sighted birds.

    Notes
    -----
    No complete,
    HackerRank 1/6 test cases failed
    """
    record = {}
    for v in arr:
        if v not in record:
            record[v] = 0
        record[v] += 1

    res = None
    curr_max = 0
    for k, v in record.items():
        if v > curr_max:
            res = k
            curr_max = v
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print('result: %s' % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
