#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
 
def sockMerchant(n, ar):
    sums = {}
    for i in ar:
        if i not in dict.keys(sums):
            sums[i] = 1
    #        print( "in locals")
        else:
            sums[i] += 1
    summ = 0
    for i in sums.values():
        summ = summ + int(i/2)
    #        print( "not in locals")
    return summ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
