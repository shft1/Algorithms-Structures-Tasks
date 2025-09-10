import sys


def solution(n, m, grid):
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp_max = 0 if i == j == 1 else max(dp[i - 1][j], dp[i][j - 1])
            dp[i][j] = dp_max + int(grid[i - 1][j - 1])
    return dp[n][m]


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    grid = [sys.stdin.readline().rstrip() for _ in range(n)][::-1]
    sys.stdout.write(str(solution(n, m, grid)))


if __name__ == "__main__":
    main()
