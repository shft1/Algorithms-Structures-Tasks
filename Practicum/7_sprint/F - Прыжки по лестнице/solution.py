import sys


def solution(n, k):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n):
        for j in range(i + 1, i + min(n - i, k) + 1):
            dp[j] = (dp[j] % MOD + dp[i] % MOD) % MOD
    return dp[n]


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(n, k)))


if __name__ == "__main__":
    main()
