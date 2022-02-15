#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
    shared = 5
    cum_liked = 0
    for i in range(n):
        liked = shared // 2
        cum_liked += liked
        shared = liked * 3
    return cum_liked


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
