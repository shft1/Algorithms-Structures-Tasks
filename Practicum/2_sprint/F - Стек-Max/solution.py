import sys


class StackMax:
    def __init__(self):
        self.item = []
        self.max_stack = []

    def push(self, x):
        self.max_stack.append(
            x if not self.item else max(x, self.max_stack[-1])
        )
        self.item.append(x)

    def pop(self):
        if self.item:
            self.item.pop()
            return self.max_stack.pop()
        sys.stdout.write("error\n")

    def get_max(self):
        sys.stdout.write(
            f"{self.max_stack[-1]}\n" if self.max_stack else "None\n"
        )


def solution():
    stack = StackMax()

    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        comd = sys.stdin.readline().rstrip()
        if comd.startswith("get_max"):
            stack.get_max()
        elif comd.startswith("pop"):
            stack.pop()
        else:
            stack.push(int(comd.split()[-1]))


if __name__ == "__main__":
    solution()
