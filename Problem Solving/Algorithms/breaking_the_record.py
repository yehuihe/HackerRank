#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    """Breaking the Records solution

    Parameters
    ----------
    scores : array-like
        Points scored per game.

    Returns
    -------
    results : array-like
        An array with the numbers of times she broke her records.
        Index  is for breaking most points records,
        and index  is for breaking least points records.
    """
    curr_min = scores[0]; curr_max = scores[0]
    min_num = 0; max_num = 0
    for score in scores[1:]:
        if score < curr_min:
            min_num += 1
            curr_min = score
        elif score > curr_max:
            max_num += 1
            curr_max = score
    return [max_num, min_num]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print('result: %s' % result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
