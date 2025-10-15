import sys


def search_nearest(signs, cj, p):
    target = cj * p
    left, right = 0, len(signs) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target == signs[mid]:
            return mid
        elif target < signs[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if left == len(signs):
        return left - 1
    if left == 0:
        return left
    if abs(signs[left - 1] / cj - p) < abs(signs[left] / cj - p):
        return left - 1
    return left


def solution(n, p, signs: list):
    keep_pos = {signs[i]: i + 1 for i in range(n)}
    signs.sort()
    min_diff = float("inf")
    pair = (None, None)
    for j in range(n):
        cj = signs[j]
        ci = signs[search_nearest(signs, cj, p)]
        if abs(ci / cj - p) < min_diff:
            min_diff = abs(ci / cj - p)
            pair = ci, cj
    return f"{keep_pos[pair[0]]} {keep_pos[pair[1]]}"


def main():
    n, p = map(int, sys.stdin.readline().rstrip().split())
    signs = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(solution(n, p, signs))


if __name__ == "__main__":
    main()
