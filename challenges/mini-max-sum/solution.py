#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    summ = 0
    for item in arr:
        if item < min:
            min = item
        if item > max:
            max = item
        summ = summ + item
    print(summ-max, summ-min) 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
