#!/bin/python3
# https://www.hackerrank.com/challenges/pylons/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pylons(k, arr):
    n = len(arr)
    start = 0
    ans = 0
    while start < n:
        curr = start + k - 1
        found = False
        while curr > start - k + 1 and curr >= 0:
            if curr < len(arr):
                if arr[curr] == 1:
                    ans += 1
                    start = curr + k
                    found = True
                    break
            curr -= 1
        if not found:
            return -1
    return ans
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(str(result) + '\n')
