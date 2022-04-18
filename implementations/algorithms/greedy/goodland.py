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
    end = k - 1
    curr = end
    ans = 0
    while curr < n:
        if arr[curr] == 0:
            hasPlace = False
            for j in range(start, end):
                if arr[j if j < n else (n - 1)] == 1:
                    start = j + 1
                    end = j + 2 * (k - 1) + 1
                    curr = end if end < n else (n - 1)
                    ans += 1
                    if start >= n:
                        break
                    hasPlace = True
                    break
            if not hasPlace:
                return -1
        else:
            start = curr + 1
            end = curr + 2 * (k - 1) + 1
            curr = end if end < n else (n - 1)
            ans += 1
            if start >= n:
                break
    return ans


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(str(result) + '\n')
