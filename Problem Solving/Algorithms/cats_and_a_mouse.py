#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    """Cats and a Mouse solution

    Parameters
    ----------
    x : int
        Cat A's position.

    y : int
        Cat B's position.

    z : int
        Mouse C's position.

    Returns
    -------
    result : str
        Either 'Cat A', 'Cat B', or 'Mouse C'
    """
    if abs(x - z) > abs(y - z):
        return "Cat B"
    elif abs(x - z) < abs(y - z):
        return "Cat A"
    else:
        return "Mouse C"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print("result: %s" % result)

        # fptr.write(result + '\n')

    # fptr.close()
