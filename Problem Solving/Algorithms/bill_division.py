#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    """Bill Division solution

    Parameters
    ----------
    bill : array-like
        An array of integers representing the cost of each item ordered.

    k : int
        An integer representing the zero-based index of the item
        Anna doesn't eat.

    b : int
        The amount of money that Anna contributed to the bill.

    Returns
    -------

    """
    _ = bill.pop(k)
    actual_bill = sum(bill) // 2
    if b == actual_bill:
        return 'Bon Appetit'
    else:
        return b - actual_bill


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))
