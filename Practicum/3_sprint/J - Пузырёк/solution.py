import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    for right in range(n, 0, -1):
        sorted = True
        for i in range(right - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        if right == n or not sorted:
            sys.stdout.write(" ".join(map(str, array)) + "\n")
        if sorted:
            return


if __name__ == "__main__":
    solution()
