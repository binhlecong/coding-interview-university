# LCA with out storing extra data
def findLCA(root, a, b):
    if root is None:
        return None
    
    if root.key == a or root.key == b:
        return root
    
    leftLca = findLCA(root.left, a, b)
    rightLca = findLCA(root.right, a, b)

    if leftLca and rightLca:
        return root

    return leftLca if rightLca is None else rightLca