import sys


def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    n_2, n_1 = 1, 1
    for _ in range(n - 1):
        n_2, n_1 = n_1, (n_1 + n_2) % 10**k
    return n_1


if __name__ == "__main__":
    sys.stdout.write(str(solution()))
