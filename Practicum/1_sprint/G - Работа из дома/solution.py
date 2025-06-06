import sys


def main():
    a, x, b, c = list(map(int, sys.stdin.readline().rstrip().split()))
    print(a * x**2 + b * x + c)
    return


if __name__ == "__main__":
    main()
