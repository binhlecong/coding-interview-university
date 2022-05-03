from itertools import permutations


def bstToArrays(root):
    arrs = [[root.data]]
    s1 = [root]
    s2 = []
    while len(s1) != 0 or len(s2) != 0:
        if len(s2) == 0:
            while len(s1) != 0:
                node = s1.pop()
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
            perms = permutations(s2)
        else:
            while len(s2) != 0:
                node = s2.pop()
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)
            perms = permutations(s1)

        n = len(arrs)
        for _ in range(n):
            pre = arrs.pop(0)
            for perm in perms:
                arrs.append(pre + perm)
