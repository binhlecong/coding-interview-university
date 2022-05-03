class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def containsTree(root1, root2):
    s1, s2 = '', ''
    s1 = treeToStr(root1)
    s2 = treeToStr(root2)
    return s2 in s1


def treeToStr(root):
    q = [root]
    ans = ''
    while len(q) > 0:
        node = q.pop()
        ans += str(node.val)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return ans
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(containsTree(root, root.right))