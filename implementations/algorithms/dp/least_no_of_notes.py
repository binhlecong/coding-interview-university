#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
# Tinh so to tien nho nhat tu 1 2 5 dollar sao cho tong bang m
notes = (5, 2, 1)
prev_ans = {}


def recursion(m, c):
    if m in prev_ans:
        return prev_ans[m]
    if m == 0:
        return c
    a = 10000000000
    for i in notes:
        if m >= i:
            a = min(a, recursion(m - i, c + 1))
    prev_ans[m] = a
    return a


def least_num_of_notes(m):
    return recursion(m, 0)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        result = least_num_of_notes(n)
        print(str(result) + '\n')
