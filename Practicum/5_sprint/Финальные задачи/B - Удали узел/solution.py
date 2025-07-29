import os
from typing import Optional

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def rightmost_node(root):
    while root.right.right:
        root = root.right
    rep_node = root.right
    root.right = rep_node.left if rep_node.left else None
    return rep_node


def leftmost_node(root):
    while root.left.left:
        root = root.left
    rep_node = root.left
    root.left = rep_node.right if rep_node.right else None
    return rep_node


def replace_node(root):
    if root.left is None and root.right is None:
        return None
    if root.left:
        l_sib = root.left
        if l_sib.right is None:
            l_sib.right = root.right
            return l_sib
        new_node = rightmost_node(l_sib)
    else:
        r_sib = root.right
        if r_sib.left is None:
            r_sib.left = root.left
            return r_sib
        new_node = leftmost_node(r_sib)
    new_node.left = root.left
    new_node.right = root.right
    return new_node


def remove(root, key) -> Optional[Node]:
    if root is None:
        return root
    if key == root.value:
        return replace_node(root)
    if key > root.value:
        root.right = remove(root.right, key)
    elif key < root.value:
        root.left = remove(root.left, key)
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == "__main__":
    test()
