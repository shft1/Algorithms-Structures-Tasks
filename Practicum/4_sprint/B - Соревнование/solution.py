import sys


def solution(arr, n):
    """
    Time: O(n)
    Mem: O(n)
    """
    prefix_diff = {}
    prefix_one, prefix_zero = 0, 0
    max_len = 0
    for i in range(n):
        if arr[i] == "1":
            prefix_one += 1
        else:
            prefix_zero += 1
        diff = prefix_one - prefix_zero
        if diff == 0:
            max_len = i + 1
        elif diff not in prefix_diff:
            prefix_diff[diff] = i
        else:
            max_len = max(max_len, i - prefix_diff[diff])
    return max_len


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    res = sys.stdin.readline().rstrip().split()
    sys.stdout.write(str(solution(res, n)) + "\n")
