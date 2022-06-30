# Given the root of a binary tree, invert the tree, and return its root.

def invertTree(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    invertTree(root.left)
    invertTree(root.right)

    return root
