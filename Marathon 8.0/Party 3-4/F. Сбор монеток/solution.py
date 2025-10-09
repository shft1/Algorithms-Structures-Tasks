import sys


def solution(n, matrix):
    prev = matrix[0]
    for i in range(1, n + 1):
        dp = [-1] * 5
        for j in range(1, 4):
            prev_max = max(prev[j - 1], prev[j], prev[j + 1])
            dp[j] = (
                prev_max + (matrix[i][j] == "C")
                if matrix[i][j] != "W" and prev_max != -1
                else -1
            )
        if max(dp) == -1:
            return max(prev)
        prev = dp
    return max(prev)


def main():
    n = int(sys.stdin.readline().rstrip())
    matrix = [[0] * 5]
    matrix.extend(
        [[-1] + list(sys.stdin.readline().rstrip()) + [-1] for _ in range(n)]
    )
    sys.stdout.write(str(solution(n, matrix)))


if __name__ == "__main__":
    main()
