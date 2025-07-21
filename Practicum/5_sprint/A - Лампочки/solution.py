import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    if root is None:
        return
    max_left = solution(root.left)
    max_right = solution(root.right)
    if max_left is None and max_right is None:
        return root.value
    if max_left is None:
        return max(root.value, max_right)
    if max_right is None:
        return max(root.value, max_left)
    return max(root.value, max_left, max_right)


def test():
    node1 = Node(-2)
    node2 = Node(-5)
    node3 = Node(-7, node1, node2)
    node4 = Node(-4, node3, None)
    assert solution(node4) == -2


if __name__ == "__main__":
    test()
