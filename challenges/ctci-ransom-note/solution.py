#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()
    for nik in note:
        if nik in magazine:
            magazine.remove(nik)
        else:
            print("No")
            return False
    print("Yes")
    return True         


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
