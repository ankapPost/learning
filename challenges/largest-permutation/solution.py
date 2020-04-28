#!/bin/python3

import math
import os
import random
import re
import sys

def largestPermutation(k, arr):
    n = len(arr)
    pos = {}
    for i in range(n):
        pos[arr[i]] = i
    
    ki = 0
    i = 0
    while (ki < k) and (i < n):
        if arr[i] == n-i:
            i = i +1
            continue
        tmp = pos[n-i]
        
        pos[arr[i]] = pos[n-i]
        pos[n-i] = i 
        
        arr[i], arr[tmp] = arr[tmp], arr[i]
        
        i = i +1
        ki = ki + 1
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
