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


# TODO: Not efficient algorithm for large grid.
#  use itertools product only work on smaller grid
def queensAttack(n, k, r_q, c_q, obstacles):

    # use itertools product only work on smaller grid

    # from itertools import product
    #
    # # Generate grid
    # grid = {}
    # for tup in product(range(1, n + 1), range(1, n + 1)):
    #     grid[tup] = "X" if tup in obstacles else 0
    #
    # # Mark queen's attack grid with obstacles
    # # vertically up
    # for i in range(r_q + 1, n + 1):
    #     if grid[(i, c_q)] == "X":
    #         break
    #     grid[(i, c_q)] += 1
    #
    # # horizontally right
    # for i in range(c_q + 1, n + 1):
    #     if grid[(r_q, i)] == "X":
    #         break
    #     grid[(r_q, i)] += 1
    #
    # # vertically down
    # for i in reversed(range(1, r_q)):
    #     if grid[(i, c_q)] == "X":
    #         break
    #     grid[(i, c_q)] += 1
    #
    # # horizontally left
    # for i in reversed(range(1, c_q)):
    #     if grid[(r_q, i)] == "X":
    #         break
    #     grid[(r_q, i)] += 1
    #
    # # diagonally lower-left
    # for i in range(1, min(r_q, c_q)):
    #     if grid[(r_q - i, c_q - i)] == "X":
    #         break
    #     grid[(r_q - i, c_q - i)] += 1
    #
    # # diagonally lower-right
    # if r_q <= n // 2:
    #     for i in range(1, r_q):
    #         if grid[(r_q - i, c_q + i)] == "X":
    #             break
    #         grid[(r_q - i, c_q + i)] += 1
    # else:
    #     for i in range(1, n - c_q + 1):
    #         if grid[(r_q - i, c_q + i)] == "X":
    #             break
    #         grid[(r_q - i, c_q + i)] += 1
    #
    # # diagonally upper-right
    # for i in range(1, n - max(r_q, c_q) + 1):
    #     if grid[(r_q + i, c_q + i)] == "X":
    #         break
    #     grid[(r_q + i, c_q + i)] += 1
    #
    # # diagonally upper-left
    # if c_q <= n // 2:
    #     for i in range(1, c_q):
    #         if grid[(r_q + i, c_q - i)] == "X":
    #             break
    #         grid[(r_q + i, c_q - i)] += 1
    # else:
    #     for i in range(1, n - r_q + 1):
    #         if grid[(r_q + i, c_q - i)] == "X":
    #             break
    #         grid[(r_q + i, c_q - i)] += 1
    #
    # # for k, v in grid.items():
    # #     print(k, v)
    #
    # count = 0
    # for v in grid.values():
    #     if v == 1:
    #         count += 1
    # return count

    # TODO: Even more efficient algorithm
    # No itertools.product solution. Still not full score
    count = 0

    # Mark queen's attack grid with obstacles
    # vertically up
    for i in range(r_q + 1, n + 1):
        if (i, c_q) in obstacles:
            break
        count += 1

    # horizontally right
    for i in range(c_q + 1, n + 1):
        if (r_q, i) in obstacles:
            break
        count += 1

    # vertically down
    for i in reversed(range(1, r_q)):
        if (i, c_q) in obstacles:
            break
        count += 1

    # horizontally left
    for i in reversed(range(1, c_q)):
        if (r_q, i) in obstacles:
            break
        count += 1

    # diagonally lower-left
    for i in range(1, min(r_q, c_q)):
        if (r_q - i, c_q - i) in obstacles:
            break
        count += 1

    # diagonally lower-right
    if r_q <= n // 2:
        for i in range(1, r_q):
            if (r_q - i, c_q + i) in obstacles:
                break
            count += 1
    else:
        for i in range(1, n - c_q + 1):
            if (r_q - i, c_q + i) in obstacles:
                break
            count += 1

    # diagonally upper-right
    for i in range(1, n - max(r_q, c_q) + 1):
        if (r_q + i, c_q + i) in obstacles:
            break
        count += 1

    # diagonally upper-left
    if c_q <= n // 2:
        for i in range(1, c_q):
            if (r_q + i, c_q - i) in obstacles:
                break
            count += 1
    else:
        for i in range(1, n - r_q + 1):
            if (r_q + i, c_q - i) in obstacles:
                break
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
        obstacles.append(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
