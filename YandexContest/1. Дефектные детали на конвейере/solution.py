import sys


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))

    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] >= k:
            lo = mid + 1
        else:
            hi = mid

    sys.stdout.write(str(lo))


if __name__ == "__main__":
    main()
