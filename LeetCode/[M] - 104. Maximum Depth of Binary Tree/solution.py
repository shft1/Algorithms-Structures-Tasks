from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# --> Solution without recursion:
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         colors = ["white"] * 201
#         stack = [root]
#         maxDepth = 0
#         currDepth = 0
#         while stack:
#             v = stack.pop()
#             if colors[v.val] == "white":
#                 colors[v.val] = "grey"
#                 stack.append(v)
#                 currDepth += 1
#                 if v.left:
#                     stack.append(v.left)
#                 if v.right:
#                     stack.append(v.right)
#             else:
#                 maxDepth = max(maxDepth, currDepth)
#                 currDepth -= 1
#         return maxDepth
