class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS


def depthFirstSearch(node):
    if node == None:
        return []
    # Using stack
    stack = [node]
    res = []
    while len(stack) > 0:
        current_node = stack.pop()
        res.append(current_node.val)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    return res
# Time O(n) Space O(n)


# BFS

def breadthFirstSearch(node):
    if node == None:
        return []

    queue = [node]
    res = []
    while len(queue) > 0:
        curr = queue.pop(0)
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return res

# Tree includes

# Iterive solution


def treeIncludes(node, target):
    if node == None:
        return False

    stack = [node]

    while len(stack) > 0:
        curr = stack.pop()

        if curr.val == target:
            return True

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return False

# Tree includes

# Recursive solution


def treeIncludes2(root, target):
    if root == None:
        return False
    if root.val == target:
        return True

    return treeIncludes2(root.left, target) or treeIncludes2(root.right, target)


a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(depthFirstSearch(a))
print(breadthFirstSearch(a))
