import sys


def binary_search(ends, start, right):
    left = 0
    nearest = 0
    while left <= right:
        mid = left + (right - left) // 2
        if ends[mid] <= start:
            left = mid + 1
            nearest = mid
        else:
            right = mid - 1
    return nearest


def solution(n):
    time_intervals = [[float("-inf"), float("-inf"), 0]] + [
        list(map(float, sys.stdin.readline().rstrip().split()))
        for _ in range(n)
    ]
    time_intervals.sort(key=lambda x: x[1])
    ends = [end for _, end, _ in time_intervals]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        start, _, weight = time_intervals[i]
        pos = binary_search(ends, start, i - 1)
        dp[i] = max(dp[i - 1], dp[pos] + weight)
    return int(dp[n]) if int(dp[n]) == dp[n] else dp[n]


def main():
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(solution(n)))


if __name__ == "__main__":
    main()
