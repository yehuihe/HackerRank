#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy_level = 100
    i = 0
    i += (i + k) % len(c)
    energy_level -= 3 if c[i] == 1 else 1
    while i != 0:
        i = (i + k) % len(c)
        energy_level -= 3 if c[i] == 1 else 1

    # Python 3.8+ Assignment expressions
    # https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
    # while (i := (i + k) % len(c)) != 0:
    #     energy_level -= 3 if c[i] == 1 else 1
    # energy_level -= 3 if c[i] == 1 else 1
    return energy_level


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
