#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    """Hourglass sum for 6 by 6 2D array

    Parameters
    ----------
    arr : arr[6][6]
        An array of integers.

    Returns
    -------
    max_sum: int
        The maximum hourglass sum.
    """
    hourglass_sums = []
    # Looping through all 5 by 5 inner array
    for i in range(1, 5):
        for j in range(1, 5):
            # For each of them calculate the sum of hourglass and add to the list
            sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + \
                  arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            hourglass_sums.append(sum)
    return max(hourglass_sums)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = hourglassSum(arr)

    print('result: %s' % result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
