m = [[1, 1, 1, 1],
        [1, -1, 1, 1],
        [1, -1, 1, 1],
        [1, -1, 1, 1],]

def isValid(m, r, c, x, y):
    return 0 <= x and x <= r - 1 and 0 <= y and y <= c - 1 and m[x][y] != -1

def findPath(m, r, c, x, y, path):
    if not isValid(m, r, c, x, y):
        return False	
    if x == r - 1 and y == c - 1:
        path.append([x, y])
        return True

    path.append([x, y])
    if findPath(m, r, c, x + 1, y, path) or findPath(m, r, c, x, y + 1, path):
        return True
    path.pop()
    return False

ans = []
print(findPath(m, 4, 4, 0, 0, ans))
print(ans)