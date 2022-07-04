"""

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):

    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]


class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
