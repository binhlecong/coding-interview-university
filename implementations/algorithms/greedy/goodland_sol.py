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
    ans = 0
    start = 0
    while start < len(arr):
        found = False
        j = start + k - 1
        while j >= start - k + 1 and j >= 0:
            if j < len(arr):
                if arr[j] == 1:
                    ans += 1
                    start = j + k
                    found = True
                    break
            j -= 1
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

