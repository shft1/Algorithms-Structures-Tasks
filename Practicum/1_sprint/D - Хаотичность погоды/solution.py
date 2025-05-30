import sys


def solution():
    """
    Time complexity: O(n)
    Memory complexity: O(n)
    """

    n = int(sys.stdin.readline().rstrip())
    measure = list(map(int, sys.stdin.readline().rstrip().split()))
    count = 0

    if n == 1:
        return 1

    if measure[0] > measure[1]:
        count += 1
    if measure[-1] > measure[-2]:
        count += 1

    for i in range(1, n - 1):
        if measure[i - 1] < measure[i] > measure[i + 1]:
            count += 1

    return count


if __name__ == "__main__":
    sys.stdout.write(str(solution()))
