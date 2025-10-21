import sys


def init_prfxs_sum(n, cheese):
    prefix_l, prefix_r = [0] * n, [0] * n
    prefix_l[0] = cheese[0]
    prefix_r[-1] = cheese[-1]
    for i in range(1, n):
        prefix_l[i] = prefix_l[i - 1] + cheese[i]
    for j in range(n - 2, -1, -1):
        prefix_r[j] = prefix_r[j + 1] + cheese[j]
    return prefix_l, prefix_r


def solution(n, cheese):
    prefix_l, prefix_r = init_prfxs_sum(n, cheese)
    min_diff, left, right = float("inf"), None, None
    l, r = 0, n - 1
    while l < r:
        diff = abs(prefix_l[l] - prefix_r[r])
        min_diff = min(min_diff, diff)
        if diff == min_diff:
            left, right = l, r
        case1 = abs(prefix_l[l + 1] - prefix_r[r])
        case2 = abs(prefix_l[l] - prefix_r[r - 1])
        if case1 < case2:
            l += 1
        else:
            r -= 1
    return min_diff, left + 1, right + 1


def main():
    n = int(sys.stdin.readline().rstrip())
    cheese = list(map(int, sys.stdin.readline().rstrip().split()))
    min_diff, l, r = solution(n, cheese)
    sys.stdout.write(f"{min_diff} {l} {r}\n")


if __name__ == "__main__":
    main()
