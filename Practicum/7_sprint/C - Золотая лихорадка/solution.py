import sys


def solution(M, gheaps):
    gheaps.sort()
    res = 0
    while M and gheaps:
        cost, weight = gheaps.pop()
        if M >= weight:
            res += cost * weight
            M -= weight
        else:
            res += cost * M
            M -= M
    return res


def main():
    M = int(sys.stdin.readline().rstrip())
    gheaps = [
        tuple(map(int, sys.stdin.readline().rstrip().split()))
        for _ in range(int(sys.stdin.readline().rstrip()))
    ]
    sys.stdout.write(str(solution(M, gheaps)))


if __name__ == "__main__":
    main()
