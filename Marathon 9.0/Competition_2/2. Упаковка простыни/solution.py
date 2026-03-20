import sys


def fit(a, b, x, y):
    cnt = 0
    while a > x:
        a = (a + 1) // 2
        cnt += 1
    while b > y:
        b = (b + 1) // 2
        cnt += 1
    return cnt


def main():
    n, m, h, w = map(int, sys.stdin.readline().rstrip().split())
    cnt1 = fit(n, m, h, w)
    cnt2 = fit(n, m, w, h)

    sys.stdout.write(str(min(cnt1, cnt2)))


if __name__ == "__main__":
    main()
