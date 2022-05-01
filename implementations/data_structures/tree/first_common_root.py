# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findLCA(root, a, b):
    routeA, routeB = [], []
    dfs(root, a, routeA)
    dfs(root, b, routeB)
    
    na, nb = len(routeA), len(routeB)
    n = na if na < nb else nb

    ans = 0
    for i in range(n):
        if routeA[i].value != routeB[i].value:
            break
        else:
            ans = i
    return routeA[ans]


def dfs(root, k, path):
    if root == None:
        return False
    path.append(root)
    if root.value == k:
        return True
    hasNode = dfs(root.left, k, path)
    if not hasNode:
        hasNode = dfs(root.right, k, path)
    if not hasNode:
        path.pop()
    return hasNode


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4, 5) = %d" % (findLCA(root, 4, 5).value))
print("LCA(4, 6) = %d" % (findLCA(root, 4, 6).value))
print("LCA(3, 4) = %d" % (findLCA(root, 3, 4).value))
print("LCA(2, 4) = %d" % (findLCA(root, 2, 4).value))
