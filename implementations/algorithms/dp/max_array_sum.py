#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    ans = 0
    n = len(arr)
    memo = [0] * n
    for i in range(0, n):
        if arr[i] > 0:
            memo[i] = max(memo[i - 1], arr[i] + memo[i - 2])
        else:
            memo[i] = max(memo[i - 1], memo[i - 2])
    return memo[n - 1]
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
