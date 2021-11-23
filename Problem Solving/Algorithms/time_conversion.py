#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """Time conversion solution

    Parameters
    ----------
    s : str
        A time in 12 hour format.

    Returns
    -------

    """
    split_clock = s[:-2].split(':')
    hh = split_clock[0]; mm = split_clock[1]; ss = split_clock[2]
    am_pm = s[-2:]
    if am_pm == 'AM':
        return str(int(hh) % 12).zfill(2) + ':' + mm + ':' +ss
    else:
        return str(12 + int(hh) % 12).zfill(2) + ':' + mm + ':' +ss


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print('result: %s' % result)

    # fptr.write(result + '\n')

    # fptr.close()
