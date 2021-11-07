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



def hourglassSum(arr):
    # Write your code here
    max_sum = -66 # to accept integer values
    row = 0 
    col =0
    while row < 4:
        proxy_arr = arr[row][col] + arr[row][col+1]+arr[row][col+2]+arr[row+1][col+1] + arr[row+2][col]+arr[row+2][col+1]+ arr[row+2][col+2]
        #consider left cell a[0][0] initially as the starting cell
        #extract the hour glass matirx
        
        #get the max sum value and compares with the remaining values
        if proxy_arr > max_sum:
            max_sum = proxy_arr
        col = col+1
        if col == 4:
            col = 0
            row = row + 1
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
