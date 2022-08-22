"""

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        # insert into the right subtree
        root.right = self.insertIntoBST(root.right, val)
    else:
        # insert into the left subtree
        root.left = self.insertIntoBST(root.left, val)
    return root
