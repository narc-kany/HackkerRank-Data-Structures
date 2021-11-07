#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    # intiliazation
    seq = [[] for _ in range(n)] # _ is a temp variable 
    #[]--> list hence [[]]--> list of list or stacked list representation
    # initliaze lastAnswer to 0
    lastAnswer = 0
    result = [] # return result (initilze a list)
    
    
    # process query operation
    # list format with 3 value per queryies
    for q,x,y in queries:
        if q == 1:
            idx = (x ^ lastAnswer) % n # ^ XOR function (A XOR B)%n
            seq[idx].append(y)
        else:
            idx = (x ^ lastAnswer) % n # ^ XOR function (A XOR B)%n
            value = y % len(seq[idx]) # length of the sequence
            lastAnswer = seq[idx][value] # 2d array index and value
            result.append(lastAnswer)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
