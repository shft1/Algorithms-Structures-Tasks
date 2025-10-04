import sys
from collections import defaultdict


def solution(string, n, m):
    a = defaultdict(list)
    for i in range(1, m + 1):
        substring = sys.stdin.readline().rstrip()
        a[substring].append(i)
    res = []
    jump = n // m
    i = 0
    while i <= len(string) - jump:
        res.append(a[string[i : i + jump]].pop())
        i += jump
    return res


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    string = sys.stdin.readline().rstrip()
    sys.stdout.write(" ".join(map(str, solution(string, n, m))))


if __name__ == "__main__":
    main()
