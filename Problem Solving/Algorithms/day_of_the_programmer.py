#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def _is_julian_leap(year):
    return True if year % 4 == 0 else False


def _is_gregorian_leap(year):
    return True if year % 400 == 0 or \
                   (year % 4 == 0 and year % 100 != 0) else False


def dayOfProgrammer(year):
    """Day of the Programmer solution

    Parameters
    ----------
    year : int
        A single integer denoting year y.

    Returns
    -------
    date : str
        Print the full date of Day of the Programmer during year
        in the format dd.mm.yyyy, where dd is the two-digit day,
        mm is the two-digit month, and yyyy is y.
    """
    d = '13'; m = '09'; y = str(year)
    if year == 1918:
        d = '26'
    elif year < 1918 and _is_julian_leap(year):
        d = '12'
    else:
        if _is_gregorian_leap(year):
            d = '12'
    return '.'.join((d, m, y))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print('result: %s' % result)

    # fptr.write(result + '\n')

    # fptr.close()
