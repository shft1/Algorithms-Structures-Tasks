import collections
from typing import Optional


# TreeNode - Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        lenQ = 1
        maxSum = root.val
        level, currLevel = 1, 0
        while queue:
            currLevel += 1
            currSum = 0
            for _ in range(lenQ):
                v = queue.popleft()
                currSum += v.val
                lenQ -= 1
                if v.left:
                    queue.append(v.left)
                    lenQ += 1
                if v.right:
                    queue.append(v.right)
                    lenQ += 1
            if currSum > maxSum:
                maxSum = currSum
                level = currLevel
        return level
