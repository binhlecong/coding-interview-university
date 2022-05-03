class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def countPaths(root, target):
    if root == None:
        return 0
    pathsFromRoot = countPathsFromRoot(root, target, 0)
    pathsOnLeft = countPaths(root.left, target)
    pathsOnRight = countPaths(root.right, target)
    return pathsFromRoot + pathsOnLeft + pathsOnRight


def countPathsFromRoot(root, target, sum):
    if root == None:
        return 0
    ans = 0
    sum += root.val
    if sum == target:
        ans += 1
    ans += countPathsFromRoot(root.left, target, sum)
    ans += countPathsFromRoot(root.right, target, sum)
    return ans


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

#     1
#    / \
#  2     3
# / \   / \
# 4 5   6 7

print(countPaths(root, 7))
