from typing import Optional


# TreeNode - Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        if root is None:
            return root
        if key == root.val:
            return self.replace_node(root)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root

    def rightmost_node(self, root):
        while root.right.right:
            root = root.right
        rep_node = root.right
        root.right = rep_node.left if rep_node.left else None
        return rep_node

    def leftmost_node(self, root):
        while root.left.left:
            root = root.left
        rep_node = root.left
        root.left = rep_node.right if rep_node.right else None
        return rep_node

    def replace_node(self, root):
        if root.left is None and root.right is None:
            return None
        if root.left:
            l_sib = root.left
            if l_sib.right is None:
                l_sib.right = root.right
                return l_sib
            new_node = self.rightmost_node(l_sib)
        else:
            r_sib = root.right
            if r_sib.left is None:
                r_sib.left = root.left
                return r_sib
            new_node = self.leftmost_node(r_sib)
        new_node.left = root.left
        new_node.right = root.right
        return new_node
