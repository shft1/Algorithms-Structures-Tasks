import sys


def solution(n, m):
    mtrx = [[0] * n for _ in range(n)]
    for _ in range(m):
        out_e, in_e = map(int, sys.stdin.readline().split())
        mtrx[out_e - 1][in_e - 1] = 1
    return mtrx


def main():
    n, m = map(int, sys.stdin.readline().split())
    matrix_adjacent = solution(n, m)
    res = [" ".join(map(str, string)) for string in matrix_adjacent]
    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    main()
