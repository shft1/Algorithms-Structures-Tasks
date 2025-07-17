import sys


def prefix_pow(a, m, s):
    length_s = len(s)
    prefix_pow = [1] * (length_s + 1)
    for i in range(length_s):
        prefix_pow[i + 1] = (prefix_pow[i] * a) % m
    return prefix_pow


def prefix_hash(a, m, s):
    length_s = len(s)
    prefix_hash = [0] * (length_s + 1)
    for i in range(length_s):
        prefix_hash[i + 1] = (prefix_hash[i] * a + ord(s[i])) % m
    return prefix_hash


def solution(prfx_h, prfx_p, m, l, r):
    return ((prfx_h[r] - prfx_h[l - 1] * prfx_p[r - l + 1]) + m) % m


def main():
    res = []
    a = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    prefix_h = prefix_hash(a, m, s)
    prefix_p = prefix_pow(a, m, s)
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().rstrip().split())
        res.append(solution(prefix_h, prefix_p, m, l, r))
    sys.stdout.write("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
