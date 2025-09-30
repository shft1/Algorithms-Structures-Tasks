import sys


def solution(a, b, c, v0, v1, v2):
    case1 = a / v0 + c / v1 + b / v2
    case2 = a / v0 + c / v0 + c / v1 + a / v2
    case3 = a / v0 + a / v1 + a / v0 + c / v0 + c / v1 + a / v1
    case4 = a / v0 + a / v1 + b / v0 + b / v1
    case5 = b / v0 + c / v1 + a / v2
    case6 = b / v0 + c / v0 + c / v1 + b / v2
    case7 = b / v0 + b / v1 + b / v0 + c / v0 + c / v1 + b / v1
    return min(case1, case2, case3, case4, case5, case6, case7)


def main():
    a, b, c, v0, v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(a, b, c, v0, v1, v2)))


if __name__ == "__main__":
    main()
