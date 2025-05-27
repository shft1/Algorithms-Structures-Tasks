import sys


def main():
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    sumi = a % 2 + b % 2 + c % 2
    if sumi == 0 or sumi == 3:
        return "WIN"
    return "FAIL"


if __name__ == "__main__":
    sys.stdout.write(main())