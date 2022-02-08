#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


# TODO: stuck
def queensAttack(n, k, r_q, c_q, obstacles):
    from itertools import product

    # Generate grid
    grid = {}
    for tup in product(range(1, n + 1), range(1, n + 1)):
        grid[tup] = 0

    # mark queen's attack grid without obstacles
    # vertically up
    for i in range(r_q + 1, n + 1):
        grid[(i, c_q)] += 1

    # horizontally right
    for i in range(c_q + 1, n + 1):
        grid[(r_q, i)] += 1

    # vertically down
    for i in range(1, r_q):
        grid[(i, c_q)] += 1

    # horizontally left
    for i in range(1, c_q):
        grid[(r_q, i)] += 1

    # diagonally lower-left
    for i in range(1, min(r_q, c_q)):
        grid[(r_q - i, c_q - i)] += 1

    # diagonally lower-right
    for i in range(1, n - c_q):
        grid[(r_q - i, c_q + i)] += 1

    # diagonally upper-right
    for i in range(1, n - min(r_q, c_q) + 1):
        grid[(r_q + i, c_q + i)] += 1

    # diagonally upper-left
    for i in range(1, n - r_q):
        grid[(r_q + i, c_q - i)] += 1

    for k, v in grid.items():
        print(k, v)

    # obstacles

    count = 0
    for v in grid.values():
        if v == 1:
            count += 1
    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
