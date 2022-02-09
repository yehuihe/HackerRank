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
    # text = s.replace(' ')
    rows = math.floor(math.sqrt(len(s)))
    columns = math.ceil(math.sqrt(len(s)))

    matrix = []
    for i in range(rows):
        matrix.append(s[i*columns:(i+1) * columns])
    print(matrix)

    #
    # encoded_message = ""
    # count = 0
    # for c in s:
    #     if count < columns:
    #         encoded_message += c
    #         count += 1
    #     else:
    #         encoded_message += ' '
    #         count = 0
    # return encoded_message


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    print("result: %s" % result)

    # fptr.write(result + '\n')

    # fptr.close()
