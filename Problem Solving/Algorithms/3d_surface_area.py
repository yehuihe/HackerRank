#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#


# TODO: Only test cases. Wrong somewhere in logic
def surfaceArea(A):
    height = len(A)
    width = len(A[0])

    # Calculate the highest z point
    max_z = 0
    for l in A:
        maximum = max(l)
        if max_z < maximum:
            max_z = maximum

    # Bottom and top equal to grid area
    bottom = top = height * width

    # Front area equals maximum sum of rows
    max_row_sum = 0
    # Side area equals sum of maximum of rows
    max_y_sum = 0
    for j in range(width):
        sum = 0
        max_y = 0
        for i in range(height):
            sum += A[i][j]
            if max_y < A[i][j]:
                max_y = A[i][j]
        if max_row_sum < sum:
            max_row_sum = sum
        max_y_sum += max_y

    print()
    print(bottom, top)
    print(max_row_sum, max_y_sum)
    # In-between hidden surface area
    hidden_area = 0
    for j in range(width):
        for i in range(1, height - 1):
            # Valley block
            if A[i][j] < A[i - 1][j] and A[i][j] < A[i + 1][j]:
                hidden_area += A[i - 1][j] - A[i][j]
                hidden_area += A[i + 1][j] - A[i][j]
    print(hidden_area)
    return bottom + top + 2 * max_row_sum + 2 * max_y_sum + hidden_area


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print("result: %s" % result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
