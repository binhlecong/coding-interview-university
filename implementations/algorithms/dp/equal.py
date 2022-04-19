#!/bin/python3
# https://www.hackerrank.com/challenges/equal/problem
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
#

def equal(arr):
    ans = 10**9
    arr.sort()
    n = len(arr)
    for base in range(3):
        current_sum = 0
        for i in range(n):
            delta = arr[i] - arr[0] + base
            current_sum += delta // 5 + delta % 5 // 2 + delta % 5 % 2 // 1
        ans = min(ans, current_sum)
    return ans 
            


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = equal(arr)
        print(str(result) + '\n')
# https://hr-testcases-us-east-1.s3.amazonaws.com/676/input00.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1650397622&Signature=SV1xNbVRfAv3KWpVD1fxNMKpZLk%3D&response-content-type=text%2Fplain
# https://hr-testcases-us-east-1.s3.amazonaws.com/676/input11.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1650397657&Signature=Z%2F5b0VBmaGOFfFD%2FPL2JHoNLPmc%3D&response-content-type=text%2Fplain