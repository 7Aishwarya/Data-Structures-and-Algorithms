#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr, n):
    t = [ [-1]*(k+1) ] * (n+1)
    for i in range(n+1):
        for j in range(k+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif arr[i-1] <= j:
                t[i][j] = max(t[i-1][j], arr[i-1] + t[i-1][j-arr[i-1]])
            else:
                t[i][j] = t[i-1][j]
    return t[i][j]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for i in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))
        length = len(arr)
        
        result = unboundedKnapsack(k, arr, length)

        fptr.write(str(result) + '\n')

    fptr.close()
