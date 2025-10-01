import sys


def solution(k, a):
    res = set(a)
    power_res = len(res)
    if power_res == k:
        return res
    if power_res > k:
        return list(res)[:k]
    if power_res < k:
        res = list(res)
        cnt = {}
        for num in a:
            cnt[num] = cnt.get(num, 0) + 1
        diff = k - power_res
        for key, value in cnt.items():
            cnt_key = value - 1
            if cnt_key <= diff:
                res.extend([key] * cnt_key)
                diff -= cnt_key
            else:
                res.extend([key] * diff)
                diff -= diff
    return res


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(" ".join(map(str, solution(k, a))) + "\n")


if __name__ == "__main__":
    main()
