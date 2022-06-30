# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia:
#
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as

# descendants (where we allow a node to be a descendant of itself).”

"""
    LCA is the last root satisfying => min(node1, node2) <= root <= max(node1,node2) 

    where q and p will be in the subtree of the root while traversing top to bottom in the tree.

"""


def lowestCommonAncestor(root, p, q):
    if root == None:
        return root
    # If both node p and node q are greater than parent
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    # If both node p and node q are less than parent
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    # We have found the split point, i.e. the LCA node.
    else:
        return root


# Time Complexity: O(log n) if the tree is balanced binary search tree.

# Otherwise, in the worst case, the complexity could be O(n)

# Space Complexity: O(n)
