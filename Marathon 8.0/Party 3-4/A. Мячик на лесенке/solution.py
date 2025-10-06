import sys


def solution(n):
    dp = [0] * (n + 3)
    dp[2] = 1
    for i in range(3, n + 3):
        dp[i] = sum(dp[i - 3 : i])
    return dp[-1]


def main():
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(solution(n)))


if __name__ == "__main__":
    main()
