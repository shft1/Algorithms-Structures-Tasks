import sys


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.power = 0

    def put(self, x):
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        self.power += 1

    def get(self):
        if not self.power:
            return sys.stdout.write("error\n")

        sys.stdout.write(f"{self.head.value}\n")
        self.head = self.head.next
        self.power -= 1

    def size(self):
        sys.stdout.write(f"{self.power}\n")


def solution():
    ll_q = QueueLinkedList()

    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        cmd = sys.stdin.readline().rstrip()
        if cmd.startswith("get"):
            ll_q.get()
        elif cmd.startswith("size"):
            ll_q.size()
        else:
            ll_q.put(int(cmd.split()[1]))


if __name__ == "__main__":
    solution()
