#!/bin/python3

import os
import sys
import itertools

#
# Complete the getMoneySpent function below.
#


def getMoneySpent(keyboards, drives, b):
    """Electronics shop solution

    Parameters
    ----------
    keyboards : array-like
        The keyboard prices.

    drives : array-like
        The drive prices.

    b : int
        The budget.

    Returns
    -------
    max_spent : int
        The maximum that can be spent, or -1 if it is
        not possible to buy both items.
    """

    spent = [
        sum(v) for v in itertools.product(keyboards, drives) if sum(v) <= b
    ]
    return max(spent) if spent else -1


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print("result: %s" % moneySpent)

    # fptr.write(str(moneySpent) + '\n')
    #
    # fptr.close()
