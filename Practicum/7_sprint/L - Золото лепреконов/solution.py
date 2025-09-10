import sys


def solution(n, M, golds):
    dp, prev_dp = [0] * (M + 1), [0] * (M + 1)
    for i in range(1, n + 1):
        for j in range(1, M + 1):
            if golds[i] <= j:
                dp[j] = max(prev_dp[j], golds[i] + prev_dp[j - golds[i]])
            else:
                dp[j] = prev_dp[j]
        prev_dp = dp
        dp = [0] * (M + 1)
    return prev_dp[M]


def main():
    n, M = map(int, sys.stdin.readline().rstrip().split())
    golds = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(n, M, golds)))


if __name__ == "__main__":
    main()
