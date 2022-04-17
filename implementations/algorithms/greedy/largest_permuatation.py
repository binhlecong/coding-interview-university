#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def largestPermutation(k, arr):
    # Write your code here
    n = len(arr)
    pos = [0] * (n + 1)
    for i in range(n):
        pos[arr[i]] = i
    for i in range(n):
        if k == 0:
            break
        maxx = n - i
        if maxx != arr[i]:
            arr[pos[maxx]], arr[i] = arr[i], arr[pos[maxx]]
            pos[arr[pos[maxx]]], pos[arr[i]] = pos[arr[i]], pos[arr[pos[maxx]]]
            k -= 1
    return arr

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    print(' '.join(map(str, result)))
    print('\n')
