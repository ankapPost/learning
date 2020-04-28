#!/bin/python3

import math
import os
import random
import re
import sys

def largestPermutation(k, arr):
    ke = 0
    while ke < k:
        max = arr[ke]
        max_index = ke
        max_found = 0
        for i in range(ke,len(arr)):
            if arr[i] > max:
                max = arr[i]
                max_index = i
                max_found = 1
        if max_found == 1:
            arr[max_index] = arr[ke]
            arr[ke] = max
            ke = ke + 1
        else:
            break
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()