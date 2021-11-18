#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

import os
import array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
        
    n, m = [int(s) for s in input().split()]           
    a = array.array('i', [int(s) for s in input().split()])
            
    for _ in range(m):
        t, i, j = [int(s) for s in input().split()]
        if t == 1:
            a = a[i-1:j] + a[:i-1] + a[j:]
        else:
            a = a[:i-1] + a[j:] + a[i-1:j]
            
    fptr.write(f'{abs(a[0] - a[-1])}\n')
    fptr.write(' '.join([str(aa) for aa in a]))
    fptr.write('\n')
    
    fptr.close()