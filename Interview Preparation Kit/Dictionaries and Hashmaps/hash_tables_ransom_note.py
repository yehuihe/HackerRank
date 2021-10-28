#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def checkMagazine(magazine, note):
    """Random Note

    Parameters
    ----------
    magazine : str
        The words in the magazine.

    note : str
        The words in the ransom note.

    Notes
    -----
    I'm not using collections.Counter. Construct your own dict.

    """
    mag_words = {}
    for word in magazine:
        if word not in mag_words:
            mag_words[word] = 0
        mag_words[word] += 1
    for word in note:
        if word not in mag_words:
            print('No')
            return
        else:
            mag_words[word] -= 1
            if mag_words[word] < 0:
                print('No')
                return
    print('Yes')
    # Alternatively, making another note_words works as well
    #
    # mag_words = {}; note_words = {}
    # for word in magazine:
    #     if word not in mag_words:
    #         mag_words[word] = 0
    #     mag_words[word] += 1
    # for word in note:
    #     if word not in note_words:
    #         note_words[word] = 0
    #     note_words[word] += 1
    # for k in note_words.keys():
    #     if k not in mag_words or note_words[k] > mag_words[k]:
    #         print('No')
    #         return
    # print('Yes')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
