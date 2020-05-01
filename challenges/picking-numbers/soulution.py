#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
#    a.sort()
    max = 0
    for i in range(len(a)):
        count = 0
        countplus = 0
        countminus =0
        for j in range(i,len(a)):
            if a[j]>=a[i] and abs(a[j]-a[i])<=1:
                countplus = countplus + 1
            if a[j]<=a[i] and abs(a[j]-a[i])<=1:
                countminus = countminus + 1
            if countplus > countminus:
                count = countplus
            else:
                count = countminus
        if count > max:
            max = count
    return max
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
