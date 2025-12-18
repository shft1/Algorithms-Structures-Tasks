from typing import Optional


# TreeNode - Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        freq = {0: 1}
        self.cnt = 0

        def searchSum(node, ps):
            if not node:
                return
            cs = ps + node.val
            x = cs - targetSum
            if x in freq:
                self.cnt += freq[x]
            if cs in freq:
                freq[cs] += 1
            else:
                freq[cs] = 1
            searchSum(node.left, cs)
            searchSum(node.right, cs)
            freq[cs] -= 1

        searchSum(root, 0)
        return self.cnt
