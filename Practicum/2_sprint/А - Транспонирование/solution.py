import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    t_matrix = [[None] * n for _ in range(m)]
    column = 0

    for _ in range(n):
        row = 0
        for s_num in sys.stdin.readline().rstrip().split():
            t_matrix[row][column] = s_num
            row += 1
        column += 1

    for string in t_matrix:
        sys.stdout.write(" ".join(string) + "\n")


if __name__ == "__main__":
    solution()
