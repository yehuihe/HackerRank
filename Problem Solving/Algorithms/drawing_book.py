#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    """Drawing book solution

    Parameters
    ----------
    n : int
        The number of pages in the book.

    p: int
        The page number to turn to.

    Returns
    -------
    min_page : int
        The minimum number of pages to turn.
    """
    return (
        min(p // 2, (n - p) // 2)
        if n % 2 != 0
        else min(p // 2, (n + 1 - p) // 2)
    )


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
