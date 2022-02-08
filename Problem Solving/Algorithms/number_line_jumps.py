#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x1, v1, x2, v2):
    """Number line jumps solution

    Parameters
    ----------
    x1 : int
        Starting position for kangaroo 1.

    v1 : int
        Jump distance for kangaroo 1.

    x2 : int
        Starting position for kangaroo 2.

    v2 : int
        Jump distance for kangaroo 2.

    Returns
    -------
    result: str
        Either YES or NO.
    """
    if x1 == x2 and v1 == v2:
        return "YES"
    elif v1 == v2:
        return "NO"
    else:
        return (
            "YES"
            if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) > 0
            else "NO"
        )


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print("result: %s" % result)

    # fptr.write(result + '\n')

    # fptr.close()
