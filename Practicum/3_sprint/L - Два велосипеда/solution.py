import sys


def binarySearch(arr, x, cur_min_idx, left, right):
    if left > right:
        return cur_min_idx

    mid = (left + right) // 2

    if arr[mid] >= x:
        return binarySearch(arr, x, cur_min_idx=mid, left=left, right=mid - 1)
    if arr[mid] < x:
        return binarySearch(arr, x, cur_min_idx, left=mid + 1, right=right)


def solution():
    n = sys.stdin.readline().rstrip()
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    x = int(sys.stdin.readline().rstrip())
    xi = binarySearch(arr, x, -2, left=0, right=len(arr) - 1)
    x2i = binarySearch(arr, x * 2, -2, left=0, right=len(arr) - 1)
    return xi, x2i


if __name__ == "__main__":
    xi, x2i = solution()
    sys.stdout.write(f"{xi+1} {x2i+1}\n")
