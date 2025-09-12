import sys


def build_dp(n, m, a, b):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def LCS(dp, n, m, a, b):
    aidx, bidx = [], []
    i, j = n, m
    while dp[i][j] != 0:
        if a[i] == b[j]:
            aidx.append(i)
            bidx.append(j)
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    aidx.reverse()
    bidx.reverse()
    return aidx, bidx


def main():
    n = int(sys.stdin.readline().rstrip())
    a = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    b = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    dp = build_dp(n, m, a, b)
    aidx, bidx = LCS(dp, n, m, a, b)
    sys.stdout.write(f"{dp[n][m]}\n")
    if dp[n][m]:
        sys.stdout.write(" ".join(map(str, aidx)) + "\n")
        sys.stdout.write(" ".join(map(str, bidx)) + "\n")


if __name__ == "__main__":
    main()
