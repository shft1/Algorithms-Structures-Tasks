from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        headEven = head.next
        tailOdd, tailEven = head, headEven
        while tailEven and tailEven.next:
            tailOdd.next = tailOdd.next.next
            tailEven.next = tailEven.next.next
            tailOdd = tailOdd.next
            tailEven = tailEven.next
        tailOdd.next = headEven
        return head
