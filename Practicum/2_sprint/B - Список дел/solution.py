import os
import sys

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node):
    while node.next_item:
        sys.stdout.write(node.value + '\n')
        node = node.next_item
    sys.stdout.write("node3" + '\n')


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
