#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    itr = iter(range(len(c)))
    count = 0
    for i in itr:
        if i+1 >= len(c):
            pass
        elif i+2 >= len(c) or c[i+2] == 0:
            count +=1
            next(itr,-1)
        elif i+1 < len(c) and c[i+1] == 0:
            count +=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
