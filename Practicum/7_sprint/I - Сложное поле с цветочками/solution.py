import sys


def solution(n, m, grid):
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp_max = 0 if i == j == 1 else max(dp[i - 1][j], dp[i][j - 1])
            dp[i][j] = dp_max + int(grid[i - 1][j - 1])
    way = []
    i, j = n, m
    while i != 1 or j != 1:
        if dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
            way.append("U")
        else:
            j -= 1
            way.append("R")
    way.reverse()
    return dp[n][m], way


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    grid = [sys.stdin.readline().rstrip() for _ in range(n)]
    grid.reverse()
    cnt, way = solution(n, m, grid)
    sys.stdout.write(f"{cnt}\n{"".join(way)}")


if __name__ == "__main__":
    main()
