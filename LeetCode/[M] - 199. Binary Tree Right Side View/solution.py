import collections
from typing import List, Optional


# TreeNode - Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        len_q = 1
        while queue:
            res.append(queue[-1].val)
            for _ in range(len_q):
                v = queue.popleft()
                len_q -= 1
                if v.left:
                    queue.append(v.left)
                    len_q += 1
                if v.right:
                    queue.append(v.right)
                    len_q += 1
        return res
