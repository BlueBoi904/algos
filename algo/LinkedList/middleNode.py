class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    length = 0
    current_node = head
    if current_node is None:
        return head

    # Traverse the list till you reach end
    while current_node:
        current_node = current_node.next
        length += 1
    node = head
    mid = length//2 + 1
    for i in range(mid - 1):
        node = node.next
    return node

# When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast.
# When fast reaches the end of the list, slow must be in the middle.


def middleNodeTwoPointer(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
