import sys


def solution(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    if x1 != x2 and y1 != y2:
        return 3 * ((abs(x1 - x2) - 1) + (abs(y1 - y2) - 1)) + 1
    if x1 == x2:
        return 3 * (abs(y1 - y2) - 1)
    if y1 == y2:
        return 3 * (abs(x1 - x2) - 1)


def main():
    x1, y1 = map(int, sys.stdin.readline().rstrip().split())
    x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(x1, y1, x2, y2)))


if __name__ == "__main__":
    main()
