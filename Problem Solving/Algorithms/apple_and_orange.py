#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """ Count apples and oranges solution

    Parameters
    ----------
    s : int
        Starting point of Sam's house location.

    t : int
        Ending location of Sam's house location.

    a : int
        Location of the Apple tree.

    b : int
        Location of the Orange tree.

    apples : array-like
        Distances at which each apple falls from the tree.

    oranges : array-like
        Distances at which each orange falls from the tree.
    """
    apples_loc = [a + unit for unit in apples]
    oranges_loc = [b + unit for unit in oranges]
    apple_count = 0
    orange_count = 0
    for loc in apples_loc:
        if loc >= s and loc <= t:
            apple_count += 1
    for loc in oranges_loc:
        if loc >= s and loc <= t:
            orange_count += 1
    print(apple_count)
    print(orange_count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
