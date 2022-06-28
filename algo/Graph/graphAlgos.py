# DFS => Stack
def depthFirstPrint(graph, source):
    stack = [source]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr)
        for neighbor in graph[curr]:
            stack.append(curr)

# DFS => Recursion


def depthFirstRecursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstRecursive(graph, neighbor)

# BFS => Queue


def breathFirstPrint(graph, source):
    queue = [source]

    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr)
        for neighbor in graph[curr]:
            queue.append(curr)


# hasPath
def hasPath(graph, src, dst):
    if src == dst:
        return True
    for item in graph[src]:
        if hasPath(graph, item, dst) == True:
            return True
    return False
