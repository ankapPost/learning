#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ap = 0
    bp = 0
    for i in range(0,3):
#        print(a[i],b[i],ap,bp)
        if a[i] > b[i]:
            ap = ap + 1
        elif a[i] < b[i]:
            bp = bp + 1
    return [ap, bp]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
