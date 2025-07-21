import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root, left=float("-inf"), right=float("inf")) -> bool:
    if root is None:
        return True
    if not (left < root.value < right):
        return False
    left_part = solution(root.left, left=left, right=root.value)
    right_part = solution(root.right, left=root.value, right=right)
    return True if left_part * right_part else False


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
