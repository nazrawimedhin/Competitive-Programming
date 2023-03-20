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
    r_grades = []
    for i in grades:
        if i <= 37:
            r_grades.append(i)
        else:
            if (i+1) % 5 == 0:
                r_grades.append(i+1)
            elif (i+2) % 5 == 0:
                r_grades.append(i+2)
            else:
                r_grades.append(i)
    return r_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
