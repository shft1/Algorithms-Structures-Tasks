import sys


def solution(n, m):
    matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    conv = {"+": 1, "-": -1}
    rows_sum, columns_sum = {}, {}
    for row in range(n):
        for column in range(m):
            symb = matrix[row][column]
            if symb == "?":
                rows_sum[row] = rows_sum.get(row, 0) + 1
                columns_sum[column] = columns_sum.get(column, 0) - 1
            else:
                rows_sum[row] = rows_sum.get(row, 0) + conv[symb]
                columns_sum[column] = columns_sum.get(column, 0) + conv[symb]
    max_rows = sorted(rows_sum.items(), key=lambda x: -x[1])
    min_column = sorted(columns_sum.items(), key=lambda x: x[1])
    max_diff = max_rows[0][1] - min_column[0][1] - 2
    for row, sum_row in max_rows:
        for column, sum_column in min_column:
            diff = sum_row - sum_column
            if matrix[row][column] in conv and diff > max_diff:
                return diff
    return max_diff


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(n, m)))


if __name__ == "__main__":
    main()
