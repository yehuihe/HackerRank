#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    """Birthday cake candles solution

    Parameters
    ----------
    candles : array-like
        The candle heights.

    Returns
    -------
    count : int
        The number of candles that are tallest.
    """
    count = 0
    max_candle = max(candles)

    i = 0
    while i < len(candles):
        if candles[i] == max_candle:
            count += 1
        i += 1
    return count



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print('result: %s' % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
