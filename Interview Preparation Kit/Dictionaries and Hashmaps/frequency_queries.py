#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    """Frequency of queries

    Parameters
    ----------
    queries : list
        A 2-d array of integers tuples. e.g.,
        [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]

    Returns
    -------
    results : list
        The results of queries of type 3.
    """

    # O(n^2) implementation using lists
    # results = []
    # arr = []
    # for operation, element in queries:
    #     if operation == 1:
    #         arr.append(element)
    #     elif operation == 2:
    #         if element in arr:
    #             arr.remove(element)
    #     else:
    #         found = False
    #         for v in set(arr):
    #             if arr.count(v) == element:
    #                 results.append(1)
    #                 found = True
    #                 break
    #         if not found:
    #             results.append(0)
    # return results

    results = []
    arr = {}
    for operation, element in queries:
        if operation == 1:
            if element not in arr:
                arr[element] = 0
            arr[element] += 1
        elif operation == 2:
            if element in arr:
                arr[element] -= 1
            else:
                pass
        else:
            results.append(1) if element in arr.values() else results.append(0)
    return results


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print("result: %s" % ans)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
