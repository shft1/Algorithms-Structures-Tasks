import sys


def check_left_diag(i, j, matrix):
    check_symb = matrix[i][j]
    cnt = 0
    for _ in range(5):
        if matrix[i][j] != check_symb:
            return False
        cnt += 1
        i += 1
        j -= 1
    return cnt == 5


def check_right_diag(i, j, matrix):
    check_symb = matrix[i][j]
    cnt = 0
    for _ in range(5):
        if matrix[i][j] != check_symb:
            return False
        cnt += 1
        i += 1
        j += 1
    return cnt == 5


def check_down(i, j, matrix):
    check_symb = matrix[i][j]
    cnt = 0
    for _ in range(5):
        if matrix[i][j] != check_symb:
            return False
        cnt += 1
        i += 1
    return cnt == 5


def check_right(i, j, matrix):
    check_symb = matrix[i][j]
    cnt = 0
    for _ in range(5):
        if matrix[i][j] != check_symb:
            return False
        cnt += 1
        j += 1
    return cnt == 5


def solution(n, m):
    matrix = [
        ["#"] + list(sys.stdin.readline().rstrip()) + ["#"] for _ in range(n)
    ]
    matrix.append(["#"] * (m + 2))
    for row in range(n):
        for column in range(1, m + 1):
            if matrix[row][column] == ".":
                continue
            if (
                check_left_diag(row, column, matrix)
                + check_right_diag(row, column, matrix)
                + check_down(row, column, matrix)
                + check_right(row, column, matrix)
            ):
                return "Yes"
    return "No"


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(solution(n, m))


if __name__ == "__main__":
    main()
