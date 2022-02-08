#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    """Min Max sum of a array

    Parameters
    ----------
    arr : array-like
        An array of 5 integers.
    """
    print(sum(arr) - max(arr), sum(arr) - min(arr))


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
