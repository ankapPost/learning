#!/bin/python3

import math
import os
import random
import re
import sys
def insertToScoresAndGetRank(scores,item):
    rank = 0
    for i in range(len(scores)):
        if i >= 1 and scores[i] == scores[i-1]:
            pass
        else:
            rank = rank + 1
        if item >= scores[i]:
            return rank
    return rank + 1

def climbingLeaderboard(scores, alice):
    alice_ranks = []
    for alice_score in alice:
        rank = insertToScoresAndGetRank(scores,alice_score)
        alice_ranks.append(rank)
        print(alice_score, scores, rank)
    return alice_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
