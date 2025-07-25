import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def is_balanced(root):
    if root is None:
        return 0
    l_deep = is_balanced(root.left)
    r_deep = is_balanced(root.right)
    if l_deep is False or r_deep is False:
        return False
    if abs(l_deep - r_deep) <= 1:
        return 1 + max(l_deep, r_deep)
    else:
        return False


def solution(root) -> bool:
    return True if is_balanced(root) else False


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == "__main__":
    test()
