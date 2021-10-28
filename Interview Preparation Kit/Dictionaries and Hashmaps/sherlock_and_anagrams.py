#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    """Count anagrams in a string

    Parameters
    ----------
    s : str
        A string.

    Returns
    -------
    anagrams : int
         The number of unordered anagrammatic pairs of substrings in S.
    """
    anagrams = 0
    char_num = 1
    while True:
        for i in range(0, len(s)):
            # if s[i:i+char_num] == s[i:i+char_num][::-1]:
            for j in range(len(s)-1, -1, -1):
                if s[i:i+char_num] =

                anagrams += 1
        char_num += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
