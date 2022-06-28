from queue import MyQueue
from stack import MyStack


def reverseK(queue, k):
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None

    # Reverse the first k elements in the queue
    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue
