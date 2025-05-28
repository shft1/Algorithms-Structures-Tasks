import sys


def main():
    """
    Time Complexity: O(1)
    Memory Complexity: O(n * m)
    """

    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    matrix = [
        list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)
    ]
    string = int(sys.stdin.readline().rstrip())
    column = int(sys.stdin.readline().rstrip())

    res = []

    if string != 0:
        res.append(matrix[string - 1][column])
    if string != n - 1:
        res.append(matrix[string + 1][column])
    if column != 0:
        res.append(matrix[string][column - 1])
    if column != m - 1:
        res.append(matrix[string][column + 1])

    res.sort()
    return res


if __name__ == "__main__":
    print(*main())
