#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    alt = 0
    itr = iter(range(n))
    undersee = 0
    valeyes = 0
    for i in itr:
        if s[i] == "D":
            alt = alt - 1
        elif s[i] == "U":
            alt = alt + 1
        
        if undersee == 0 and alt < 0:
            undersee = 1
            valeyes += 1
        if undersee == 1 and alt >= 0:
            undersee = 0

        print(i,s[i],alt,undersee,valeyes)
    return valeyes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
