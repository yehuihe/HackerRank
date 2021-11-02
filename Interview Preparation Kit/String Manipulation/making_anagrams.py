#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    """Anagram encryption scheme

    Parameters
    ----------
    a : str
        A string.

    b : str
        Another string.

    Returns
    -------
    result : int
        The minimum total characters that must be deleted.
    """
    from collections import Counter

    count_a = Counter(a)
    count_b = Counter(b)
    # count_a.subtract(count_b)
    return sum(abs(v) for v in count_a.values())


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print('result: %s' % res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
