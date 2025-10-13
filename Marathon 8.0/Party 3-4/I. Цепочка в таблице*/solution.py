import sys


def DFS(i, j, matrix, dp, colors):
    stack = []
    stack.append((i, j))
    max_seq_el = 0
    while stack:
        i, j = stack.pop()
        if colors[i][j] == "white":
            colors[i][j] = "grey"
            stack.append((i, j))
            for xd, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if matrix[i + xd][j + dy] == matrix[i][j] + 1:
                    stack.append((i + xd, j + dy))
        elif colors[i][j] == "grey":
            max_len = 1
            for xd, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if matrix[i + xd][j + dy] == matrix[i][j] + 1:
                    max_len = max(max_len, 1 + dp[i + xd][j + dy])
            dp[i][j] = max_len
            max_seq_el = max(max_seq_el, max_len)
            colors[i][j] = "black"
    return max_seq_el


def solution(n, m, matrix):
    colors = [["white"] * (m + 2) for _ in range(n + 2)]
    dp = [[0] * (m + 2) for _ in range(n + 2)]
    max_chain = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            max_chain = max(max_chain, DFS(i, j, matrix, dp, colors))
    return max_chain


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    matrix = [[0] * (m + 2)]
    matrix.extend(
        [
            [0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0]
            for _ in range(n)
        ]
    )
    matrix.append([0] * (m + 2))
    sys.stdout.write(str(solution(n, m, matrix)))


if __name__ == "__main__":
    main()
