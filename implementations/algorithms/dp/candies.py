# https://www.hackerrank.com/challenges/candies/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def candies(n, arr):
    s = [0] * n
    c = [0] * n
    for i in range(n):
        if s[i - 1] != 1 and i > 0:
            s[i] = s[i - 1] - 1
        else:
            s[i] = get_len_decreasing(n, arr, i)

        if arr[i] > arr[i - 1]:
            c[i] = max(s[i], c[i - 1] + 1)
        else:
            c[i] = s[i]
    return sum(c)


def get_len_decreasing(n, arr, i):
    ret = 1
    while i + 1 < len(arr):
        if arr[i] > arr[i+1]:
            ret += 1
            i += 1
        else:
            return ret
    return ret


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)
# 10
# 2
# 4
# 2
# 6
# 1
# 7
# 8
# 9
# 2
# 1
# Here is the way I approached this problem.

# Let S[i] = The length of decreasing sequence that begins with the i-th element of the given ratings array. If there is no decreasing sequence beginning at i, S[i] = 1 by default.

# Let C[i] = the minimum no. of candies given to the i-th student. The ultimate solution we want is sum(C[i]) for all i.

# Key insight: C[i] = S[i] for all i, EXCEPT when ratings[i] > ratings[i-1], in which case C[i] = max(S[i], C[i-1]+1).

# As an example, consider a ratings array like [4, 4, 2, 3, 4, 1]. The corresponding S array would be: S = [1, 2, 1, 1, 2, 1] The corresponding C array is: C = [1, 2, 1, 2, 3, 1] Solution: sum(C) = 10.

# (Also note that it is not necessary to compute S[i] from scratch for every i. If S[i-1] > 1, then S[i] = S[i-1] - 1. This improves efficiency.)
