#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encryption(s):
    rows = math.floor(math.sqrt(len(s)))
    columns = math.ceil(math.sqrt(len(s)))
    if rows * columns < len(s):
        rows += 1

    matrix = []
    for i in range(rows):
        matrix.append(s[i * columns : (i + 1) * columns])

    encoded_message = ""
    for i in range(columns):
        for j in range(rows):
            try:
                encoded_message += matrix[j][i]
            except IndexError:
                encoded_message += " "

    temp_matrix = []
    for i in range(columns):
        temp_matrix.append(encoded_message[i * rows : (i + 1) * rows])
    temp_matrix = [s.strip() for s in temp_matrix]
    return " ".join(temp_matrix)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    print("result: %s" % result)

    # fptr.write(result + '\n')

    # fptr.close()
