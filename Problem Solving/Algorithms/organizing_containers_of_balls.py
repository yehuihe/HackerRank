#!/bin/python3
import copy
import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

# TODO: No idea
def one_zero_swap(matrix):
    temp_matrix = matrix.copy()

    temp_matrix[0][0] += 1
    temp_matrix[0][1] -= 1

    temp_matrix[1][0] -= 1
    temp_matrix[1][1] += 1

    if temp_matrix[0][1] == 0 and temp_matrix[1][0] == 0:
        return True
    return False


def zero_one_swap(matrix):
    temp_matrix = matrix.copy()

    temp_matrix[0][0] -= 1
    temp_matrix[0][1] += 1

    temp_matrix[1][0] += 1
    temp_matrix[1][1] -= 1

    if temp_matrix[0][0] == 0 and temp_matrix[1][1] == 0:
        return True
    return False


def organizingContainers(container):
    print(container)

    for swap in (one_zero_swap, zero_one_swap):
        if swap(container):
            return "Possible"
    return "Impossible"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print("result: %s" % result)

        # fptr.write(result + '\n')

    # fptr.close()
