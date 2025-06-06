import sys


def solution():
    s = sorted(sys.stdin.readline().rstrip())
    t = sorted(sys.stdin.readline().rstrip())

    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]

    return t[-1]


if __name__ == "__main__":
    sys.stdout.write(solution())
