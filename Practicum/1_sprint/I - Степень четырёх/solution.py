import sys


def solution():
    """
    Time complexity: O(log4(n))
    Memory complexity: O(1)
    """

    num = int(sys.stdin.readline().rstrip())
    i = 0

    while 4**i <= num:
        if 4**i == num:
            return True
        i += 1
    return False


if __name__ == "__main__":
    sys.stdout.write(str(solution()))
