#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack = [(p[0], 0)]
    maxN = 0
    for i in range(1, len(p)):
        if (p[i] > p[i - 1]):
            stack.append((p[i], 1))
            maxN = max((maxN, 1))
        else:
            n = 0
            while (len(stack) > 0 and stack[-1][0] >= p[i]):
                n = max((n, stack[-1][1]))
                stack.pop()
            dayToDie = 0 if len(stack) == 0 else n + 1
            maxN = max((maxN, dayToDie))

            stack.append((p[i], dayToDie))
    return maxN

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
