# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cnt = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.search_goodNodes(root.val, root)
        return self.cnt

    def search_goodNodes(self, maxVal, node):
        if not node:
            return
        if node.val >= maxVal:
            self.cnt += 1
            maxVal = node.val
        self.search_goodNodes(maxVal, node.left)
        self.search_goodNodes(maxVal, node.right)
