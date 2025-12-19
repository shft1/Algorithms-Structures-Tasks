from typing import Optional


# TreeNode - Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.searchZigZag(root.left, "r", 1)
        self.searchZigZag(root.right, "l", 1)
        return self.res

    def searchZigZag(self, node, direction, curr):
        if not node:
            return
        if direction == "r":
            self.searchZigZag(node.left, "r", 1)
            self.searchZigZag(node.right, "l", curr + 1)
        elif direction == "l":
            self.searchZigZag(node.left, "r", curr + 1)
            self.searchZigZag(node.right, "l", 1)
        self.res = max(self.res, curr)
