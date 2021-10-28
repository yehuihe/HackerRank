#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def twoStrings(s1, s2):
    """Substring detection between strings

    Parameters
    ----------
    s1 : str
        First string.

    s2 : str
        Second string

    Returns
    -------
    string : {'YES', 'NO'}
    """
    for c1 in s1:
        if c1 in s2:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print('result: %s' % result)
        # fptr.write(result + '\n')

    # fptr.close()
