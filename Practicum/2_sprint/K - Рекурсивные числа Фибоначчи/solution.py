import sys


def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def solution():
    n = int(sys.stdin.readline().rstrip())
    return fibonacci(n)


if __name__ == "__main__":
    sys.stdout.write(str(solution()))
