import sys
from bisect import bisect_right


def build_prefix_sum(arr, n):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    return prefix_sum


def sum_for_ai(n, ai, m, sort_bj, prfx_sum_bj):
    si = 0
    for i in range(n):
        insert_idx = bisect_right(sort_bj, ai[i])
        K1, Q1 = insert_idx, m - insert_idx
        sum_bk1 = prfx_sum_bj[insert_idx]
        sum_bq1 = prfx_sum_bj[m] - prfx_sum_bj[insert_idx]
        si += (i + 1) * (ai[i] * (K1 - Q1) + sum_bq1 - sum_bk1)
    return si


def sum_for_bj(m, bj, n, sort_ai, prfx_sum_ai):
    sj = 0
    for j in range(m):
        insert_idx = bisect_right(sort_ai, bj[j])
        K2, Q2 = insert_idx, n - insert_idx
        sum_ak2 = prfx_sum_ai[insert_idx]
        sum_aq2 = prfx_sum_ai[n] - prfx_sum_ai[insert_idx]
        sj += (j + 1) * (bj[j] * (K2 - Q2) + sum_aq2 - sum_ak2)
    return sj


def solution(n, ai, m, bj):
    sort_ai, sort_bj = sorted(ai), sorted(bj)
    prfx_sum_ai = build_prefix_sum(sort_ai, n)
    prfx_sum_bj = build_prefix_sum(sort_bj, m)
    si = sum_for_ai(n, ai, m, sort_bj, prfx_sum_bj)
    sj = sum_for_bj(m, bj, n, sort_ai, prfx_sum_ai)
    return si - sj


def main():
    n = int(sys.stdin.readline().rstrip())
    ai = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    bj = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(n, ai, m, bj)))


if __name__ == "__main__":
    main()
