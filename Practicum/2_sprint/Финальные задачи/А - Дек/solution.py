import sys


class CircularBufferedDequeue:
    def __init__(self, m):
        self.items = [None] * m
        self.size = 0
        self.max_size = m
        self.front_p = m // 2
        self.back_p = self.front_p - 1

    def push_back(self, value):
        if self.size == self.max_size:
            sys.stdout.write("error\n")
            return

        self.back_p = (self.back_p + 1) % self.max_size
        self.items[self.back_p] = value
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            sys.stdout.write("error\n")
            return

        self.front_p = (
            self.max_size - 1 if self.front_p == 0 else self.front_p - 1
        )
        self.items[self.front_p] = value
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            sys.stdout.write("error\n")
            return

        sys.stdout.write(f"{self.items[self.back_p]}\n")
        self.items[self.back_p] = None
        self.size -= 1
        self.back_p = (
            self.max_size - 1 if self.back_p == 0 else self.back_p - 1
        )

    def pop_front(self):
        if self.size == 0:
            sys.stdout.write("error\n")
            return

        sys.stdout.write(f"{self.items[self.front_p]}\n")
        self.items[self.front_p] = None
        self.size -= 1
        self.front_p = (self.front_p + 1) % self.max_size


def solution():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    dequeue = CircularBufferedDequeue(m)

    for _ in range(n):
        cmd = sys.stdin.readline().rstrip()
        if cmd.startswith("push_back"):
            dequeue.push_back(int(cmd.split()[1]))
        elif cmd.startswith("push_front"):
            dequeue.push_front(int(cmd.split()[1]))
        elif cmd.startswith("pop_back"):
            dequeue.pop_back()
        else:
            dequeue.pop_front()


if __name__ == "__main__":
    solution()
