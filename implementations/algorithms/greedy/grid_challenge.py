# https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    n = len(grid)
    for i in range(n):
        sorted_characters = sorted(grid[i])
        a_string = "".join(sorted_characters)
        grid[i] = a_string
        
    isSwapped = True
    while isSwapped:
        isSwapped = False
        for j in range(1, n):
            if grid[j - 1][0] > grid[j][0]:
                grid[j], grid[j - 1] = grid[j - 1], grid[j]
                isSwapped = True
        
    for i in range(1, n):
        isSwapped = True
        while isSwapped:
            isSwapped = False
            for j in range(1, n):
                if grid[j - 1][i] > grid[j][i]:
                    if grid[j - 1][i - 1] != grid[j][i - 1]:
                        return 'NO'
                    grid[j], grid[j - 1] = grid[j - 1], grid[j]
                    isSwapped = True
                    
    return 'YES'

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(grid)
        print(result, end='\n')
