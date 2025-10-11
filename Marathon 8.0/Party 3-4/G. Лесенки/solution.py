import sys


def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for odd in range(1, n + 1, 2):
        for i in range(odd, n + 1):
            dp[i] += dp[i - odd]
    return dp[n]


def main():
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(solution(n)))


if __name__ == "__main__":
    main()
