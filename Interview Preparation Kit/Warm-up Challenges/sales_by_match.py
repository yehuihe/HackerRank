#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    """sockMerchant function

    Parameters
    ----------
    n : int
        The number of socks in the pile.
    ar : list
        The colors of each sock.

    Returns
    -------
    pairs: int
        The number of pairs.
    """
    pairs = 0
    sock_colors = set()
    for i, v in enumerate(ar):
        if v not in sock_colors:
            count = 0
            for j in range(i, n):
                if ar[j] == v:
                    count += 1
            pairs += count // 2
            sock_colors.add(v)
    return pairs
    # One liner
    # return sum([ar.count(i) // 2 for i in set(ar)])


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
