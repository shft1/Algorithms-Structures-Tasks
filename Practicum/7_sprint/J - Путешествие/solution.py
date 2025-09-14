import sys


def solution(n, a):
    dp = [1 for _ in range(n + 1)]
    prev = [-1 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    maxi, idx = 0, 0
    for i in range(1, n + 1):
        if dp[i] > maxi:
            maxi, idx = dp[i], i
    el = []
    while idx != -1:
        el.append(idx)
        idx = prev[idx]
    el.reverse()
    return maxi, el


def main():
    n = int(sys.stdin.readline().rstrip())
    a = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    size, el = solution(n, a)
    sys.stdout.write(f"{size}\n")
    sys.stdout.write(" ".join(map(str, el)))


if __name__ == "__main__":
    main()
