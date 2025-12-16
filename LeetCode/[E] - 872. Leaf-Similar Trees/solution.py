from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        leafes1, leafes2 = [], []
        self.leafes_collect(root1, leafes1)
        self.leafes_collect(root2, leafes2)
        return leafes1 == leafes2

    def leafes_collect(self, node, leafes):
        if not node:
            return
        if not node.left and not node.right:
            return leafes.append(node.val)
        self.leafes_collect(node.left, leafes)
        self.leafes_collect(node.right, leafes)
