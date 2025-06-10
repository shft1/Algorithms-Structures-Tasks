import sys


class MyQueueSized:
    def __init__(self, n):
        self.elements = [None] * n
        self.head = 0
        self.tail = 0
        self.cur_size = 0
        self.max_size = n

    def push(self, x):
        if self.cur_size == self.max_size:
            return sys.stdout.write("error\n")
        self.elements[self.tail] = x
        self.cur_size += 1
        self.tail = (self.tail + 1) % self.max_size

    def pop(self):
        if not self.cur_size:
            return sys.stdout.write("None\n")
        x = self.elements[self.head]
        self.elements[self.head] = None
        self.cur_size -= 1
        self.head = (self.head + 1) % self.max_size
        sys.stdout.write(f"{x}\n")

    def peek(self):
        if not self.cur_size:
            return sys.stdout.write("None\n")
        sys.stdout.write(f"{self.elements[self.head]}\n")

    def size(self):
        sys.stdout.write(f"{self.cur_size}\n")


def solution():
    count_cmd = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    rb_queue = MyQueueSized(n)

    for _ in range(count_cmd):
        cmd = sys.stdin.readline().rstrip()
        if cmd.startswith("pop"):
            rb_queue.pop()
        elif cmd.startswith("peek"):
            rb_queue.peek()
        elif cmd.startswith("size"):
            rb_queue.size()
        else:
            rb_queue.push(int(cmd.split()[1]))


if __name__ == "__main__":
    solution()
