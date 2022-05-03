# LCA with out storing extra data
def findLCA(root, a, b):
    if root is None:
        return None
    # A child node is found
    if root.key == a or root.key == b:
        return root
    
    leftLca = findLCA(root.left, a, b)
    rightLca = findLCA(root.right, a, b)
    # The common root is found
    if leftLca and rightLca:
        return root
    #
    return leftLca if rightLca is None else rightLca