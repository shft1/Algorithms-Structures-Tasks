import sys


def create_prefix_sum(n, arr):
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum


def solution(n, m, k, defects):
    prefix_sum = [0] + create_prefix_sum(n, defects)
    diffs_array = [0] * (n + 1)
    sum_discomfort = 0
    for _ in range(m):
        l, r = map(int, sys.stdin.readline().rstrip().split())
        diffs_array[l - 1] += 1
        diffs_array[r] -= 1
        sum_discomfort += prefix_sum[r] - prefix_sum[l - 1]
    cnts_m = create_prefix_sum(n, diffs_array)
    source = sorted([(cnts_m[i], defects[i]) for i in range(n)], reverse=True)
    p = 0
    while p != n and k != 0:
        cnt_m, defect = source[p]
        if k >= defect:
            sum_discomfort -= defect * cnt_m
            k -= defect
        else:
            sum_discomfort -= k * cnt_m
            k = 0
        p += 1
    return sum_discomfort


def main():
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    defects = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(n, m, k, defects)))


if __name__ == "__main__":
    main()
