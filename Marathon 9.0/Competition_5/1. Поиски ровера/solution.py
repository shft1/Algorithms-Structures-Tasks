import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    L = -(10**18)
    R = 10**18
    for _ in range(n):
        xi, di = map(int, sys.stdin.readline().split())
        L = max(L, xi - di)
        R = min(R, xi + di)
    if L > R:
        print(-1)
    else:
        print(R)


if __name__ == "__main__":
    main()
