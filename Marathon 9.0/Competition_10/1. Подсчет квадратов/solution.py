import sys


def solve():
    n, m = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    visited = [list(row) for row in grid]
    bacteria_count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == "#":
                bacteria_count += 1
                size = 1
                while (
                    i + size < n
                    and j + size < m
                    and all(
                        visited[i + k][j + size] == "#"
                        for k in range(size + 1)
                    )
                    and all(
                        visited[i + size][j + k] == "#" for k in range(size)
                    )
                ):
                    size += 1
                for row in range(i, i + size):
                    for col in range(j, j + size):
                        visited[row][col] = "."

    print(bacteria_count)


if __name__ == "__main__":
    solve()
