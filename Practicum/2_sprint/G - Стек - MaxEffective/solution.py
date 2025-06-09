import sys


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.maxis = []

    def push(self, x):
        self.maxis.append(x if not self.items else max(self.maxis[-1], x))
        self.items.append(x)

    def pop(self):
        if not self.items:
            sys.stdout.write("error\n")
        else:
            self.items.pop()
            self.maxis.pop()

    def get_max(self):
        sys.stdout.write("None\n" if not self.maxis else f"{self.maxis[-1]}\n")

    def top(self):
        if not self.items:
            sys.stdout.write("error\n")
        else:
            sys.stdout.write(f"{self.items[-1]}\n")


def solution():
    stack = StackMaxEffective()

    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        cmd = sys.stdin.readline().rstrip()
        if cmd.startswith("pop"):
            stack.pop()
        elif cmd.startswith("get_max"):
            stack.get_max()
        elif cmd.startswith("top"):
            stack.top()
        else:
            stack.push(int(cmd.split()[1]))


if __name__ == "__main__":
    solution()
