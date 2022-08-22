"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    res = ListNode()
    prev = res
    curr1 = list1
    curr2 = list2

    while curr1 and curr2:
        if curr1.val < curr2.val:
            res.next = curr1
            curr1 = curr1.next
        else:
            res.next = curr2
            curr2 = curr2.next
        res = res.next
    if curr1 is None:
        res.next = curr2

    if curr2 is None:
        res.next = curr1

    return prev.next
