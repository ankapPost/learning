#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(0,len(arr)):
#        print(arr[i][i],arr[i][ -(i+1)])
        sum1 = sum1 + arr[i][i]
        sum2 = sum2 + arr[i][ -(i+1)]
    return abs(sum1-sum2)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
