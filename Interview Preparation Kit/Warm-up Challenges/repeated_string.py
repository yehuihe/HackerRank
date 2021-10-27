#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    """Find repeated string

    Parameters
    ----------
    s : str
        A string to repeat.
    n : int
        The number of characters to consider.

    Returns
    -------
    count : int
        The frequency of a in the substring.
    """
    # formula for counting is: freq(a) * n // len(s) for fully repeated string
    # adding partial string with length n mod len(s)
    return s.count('a') * (n // len(s)) + s[0:n % len(s)].count('a')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print('result: %s' % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
