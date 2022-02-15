#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#


# TODO: Error: one test case failed.
def acmTeam(topic):
    n = len(topic)
    m = len(topic[0])

    num_of_topics = [
        m - str(int(topic[i]) + int(topic[j])).count("0")
        for i in range(n - 1)
        for j in range(i + 1, n)
    ]
    max_num = max(num_of_topics)
    return [max_num, num_of_topics.count(max_num)]


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print("result: %s" % result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
