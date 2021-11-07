#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

Rows = 5
Columns = 5

def hourglassSum(arr):
    # Write your code here
    max_sum = -5000;
    if(Rows<3 or Columns<3):
           return -1
    for i in range(0, Rows-2):
        for j in range(0, Columns-2):
           sum_value = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
        if(sum_value > max_sum):
            max_sum = sum_value
        else:
            continue
    
    return max_sum

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
