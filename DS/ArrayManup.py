#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    # initilize array element
    # brute force approach
    arr = [0] * (n+2) # its only a single matirx and to avoid out of bound error
    # if its 4th element our operation is performed on the 5th element hence n+2
    # perfrom query operations for p[start index], q, k in queries
    for p,q,k in queries:
        arr[p] = arr[p] + k
        arr[q + 1] = arr[q + 1] - k
        
        # find max element in the array
        max_value = _ = 0  # _ is temp value
        for val in arr:
            _ = _ + val
            max_value = max(_, max_value)
            
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
