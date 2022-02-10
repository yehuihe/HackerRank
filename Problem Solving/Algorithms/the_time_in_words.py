#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

number_str = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "quarter",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "ninety",
    20: "twenty",
    21: "twenty one",
    22: "twenty two",
    23: "twenty three",
    24: "twenty four",
    25: "twenty five",
    26: "twenty six",
    27: "twenty seven",
    28: "twenty eight",
    29: "twenty nine",
    30: "half",
}


def timeInWords(h, m):
    if m == 0:
        return f"{number_str[h]} o' clock"
    elif m == 1:
        return f"{number_str[m]} minute past {number_str[h]}"
    elif m in (15, 30):
        return f"{number_str[m]} past {number_str[h]}"
    elif 1 <= m < 30:
        return f"{number_str[m]} minutes past {number_str[h]}"
    elif m == 45:
        return f"{number_str[60-m]} to {number_str[h+1]}"
    elif 30 < m <= 59:
        return f"{number_str[60-m]} minutes to {number_str[h+1]}"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print("result: %s" % result)

    # fptr.write(result + '\n')

    # fptr.close()
