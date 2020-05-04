#!/bin/python3

import math
import os
import random
import re
import sys

def scoresToRanks(scores):
    ranks = []
    rank = 0
    myIter = iter(range(len(scores)))
    for i in myIter:
        if i >= 1 and scores[i] == scores[i-1]:
            pass
        else:
            rank += 1
        ranks.append(rank)
#        print(i,scores[i],rank)
    return ranks

def insertToScores(scores,item):
    for i in range(len(scores)):
        if item > scores[i]:
            scores.insert(i,item)
            return i
    scores.insert(i+1,item)
    return i+1

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_ranks = []
    for alice_score in alice:
        index = insertToScores(scores,alice_score)
        alice_ranks.append(scoresToRanks(scores)[index])
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
