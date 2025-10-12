import sys


def solution(n):
    return 2 if n % 4 == 0 else 1


def main():
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(solution(n)))


if __name__ == "__main__":
    main()
