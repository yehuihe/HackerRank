#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    """Grading students solution

    Parameters
    ----------
    grades : array-like
        The grades before rounding.

    Returns
    -------
    final_grade: array-like
        The grades after rounding as appropriate.
    """
    final_grade = []
    for grade in grades:
        next_mul_of_five = (grade // 5 + 1) * 5
        if grade < 38:
            final_grade.append(grade)
        elif next_mul_of_five - grade < 3:
            final_grade.append(next_mul_of_five)
        else:
            final_grade.append(grade)
    return final_grade



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('result: %s' % result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
