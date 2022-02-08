#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def binary_search(A, n, T):
    L = 0
    R = n - 1
    while L <= R:
        m = (L + R) // 2
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return m
    return None


def whatFlavors(cost, money):
    """Ice cream parlor solution

    Parameters
    ----------
    cost : array-like
        The prices for each flavor in int.

    money : int
        The amount of money they have to spend.
    """
    record = {}
    for i, v in enumerate(cost):
        if money - v in record:
            print(record[money - v], i + 1)
        record[v] = i + 1

    # O(n^2) solution. Not suitable for HackerRank
    # for i in range(len(cost)):
    #     for j in range(i+1, len(cost)):
    #         if cost[i] + cost[j] == money:
    #             print(i+1, j+1)


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
