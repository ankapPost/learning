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

def getNextMultipleOf5 (grade):
    return (int(grade/5) + 1) * 5

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] + 3 < 40:
            print(grades[i], "continue")
            continue
        elif getNextMultipleOf5(grades[i]) - grades[i] < 3:
            print(grades[i], getNextMultipleOf5(grades[i]))
            grades[i] = getNextMultipleOf5(grades[i])
    return grades
    # Write your code here

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
