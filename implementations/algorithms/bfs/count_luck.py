#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def countLuck(matrix, k):
    # Find starting point
    rows = len(matrix)
    cols = len(matrix[0])
    startX = 0
    startY = 0
    finishX = 0
    finishY = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'M':
                startX, startY = i, j
            elif matrix[i][j] == '*':
                finishX, finishY = i, j
    # BFS
    visit = []
    for i in range(rows):
        visit.append([False] * cols)
    trace = [[(i, j) for j in range(cols)] for i in range(rows)]
    cells = []
    cells.append((startX, startY))
    visit[startX][startY] = True
    while len(cells) != 0:
        current = cells.pop(0)
        for direction in directions:
            nextCell = (current[0] + direction[0], current[1] + direction[1])
            if nextCell[0] < 0 or nextCell[0] >= rows or nextCell[1] < 0 or nextCell[1] >= cols:
                continue
            if visit[nextCell[0]][nextCell[1]]:
                continue
            if matrix[nextCell[0]][nextCell[1]] == '.':
                trace[nextCell[0]][nextCell[1]] = (current[0], current[1])
                visit[nextCell[0]][nextCell[1]] = True
                cells.append((nextCell[0], nextCell[1]))
            elif matrix[nextCell[0]][nextCell[1]] == '*':
                trace[nextCell[0]][nextCell[1]] = (current[0], current[1])
                visit[nextCell[0]][nextCell[1]] = True
                cells.append((nextCell[0], nextCell[1]))
                cells.clear()
                break
    decision = 0
    finishX = trace[finishX][finishY][0]
    finishY = trace[finishX][finishY][1]
    print('trace', trace)
    while True:
        choice = 0
        if matrix[finishX][finishY] == 'M':
            choice = 1
        for direction in directions:
            nextCell = (finishX + direction[0], finishY + direction[1])
            if nextCell[0] < 0 or nextCell[0] >= rows or nextCell[1] < 0 or nextCell[1] >= cols:
                continue
            if matrix[nextCell[0]][nextCell[1]] == '.' or matrix[nextCell[0]][nextCell[1]] == 'M' or matrix[nextCell[0]][nextCell[1]] == '*':
                choice += 1
        if choice > 2:
            decision += 1
        _finishX = finishX
        finishX = trace[finishX][finishY][0]
        finishY = trace[_finishX][finishY][1]
        if finishX == trace[finishX][finishY][0] and finishY == trace[finishX][finishY][1]:
            break
    choice = 0
    if matrix[finishX][finishY] == 'M':
        choice = 1
    for direction in directions:
        nextCell = (finishX + direction[0], finishY + direction[1])
        if nextCell[0] < 0 or nextCell[0] >= rows or nextCell[1] < 0 or nextCell[1] >= cols:
            continue
        if matrix[nextCell[0]][nextCell[1]] == '.' or matrix[nextCell[0]][nextCell[1]] == 'M' or matrix[nextCell[0]][nextCell[1]] == '*':
            choice += 1
    if choice > 2:
        decision += 1

    return 'Impressed' if decision == k else 'Oops!'


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        matrix = []
        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)
        k = int(input().strip())
        result = countLuck(matrix, k)
        print(result)

# pass 4/8
