class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    fast, slow = head, head

    while fast and fast.next:
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
