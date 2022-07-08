# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        def helper(root, depth=0):
            if root is None:
                return 0

            left = helper(root.left, depth + 1)
            right = helper(root.right, depth + 1)

            return 1 + max(left, right)

        return helper(root)
