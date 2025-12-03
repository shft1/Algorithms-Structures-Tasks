import sys


def main():
    MOD = 10**9 + 7
    M, N = map(int, sys.stdin.readline().strip().split())
    W = list(map(int, sys.stdin.readline().strip().split()))
    diff = sum(W) - M
    left, right = 0, max(W)
    while left < right:
        mid = (left + right) // 2
        s = 0
        for w in W:
            if w < mid:
                s += w
            else:
                s += mid
        if s >= diff:
            right = mid
        else:
            left = mid + 1
    t = left
    b = t - 1
    base_sum = 0
    for w in W:
        if w <= b:
            base_sum += w
        else:
            base_sum += b
    rest = diff - base_sum
    res = 0
    for w in W:
        if w <= b:
            d = w
        else:
            if rest > 0:
                d = b + 1
                rest -= 1
            else:
                d = b
        res = (res + (d * d) % MOD) % MOD
    sys.stdout.write(str((res % MOD)))


if __name__ == "__main__":
    main()
