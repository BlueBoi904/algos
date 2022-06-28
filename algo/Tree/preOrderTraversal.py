"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root):
    if root is None:
        return []

    def preorder(node):
        res.append(node.val)
        for node in node.children:
            if node is not None:
                preorder(node)

    res = []
    preorder(root)
    return res
