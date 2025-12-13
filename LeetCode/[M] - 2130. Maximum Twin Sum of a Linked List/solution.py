from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = ListNode(next=head)
        slow, fast = prev, prev
        half = []
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            half.append(slow.val)
        twin = len(half) - 1
        slow = slow.next
        maxSum = 0
        while slow:
            maxSum = max(maxSum, slow.val + half[twin])
            twin -= 1
            slow = slow.next
        return maxSum
