import sys


def init_prefix_sum(n, prof, x):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (prof[i - 1] >= x)
    return prefix_sum


def solution(n, x, prof, m):
    prfx_sum = init_prefix_sum(n, prof, x)
    p = 0
    res = []
    for _ in range(m):
        cmds = list(map(int, sys.stdin.readline().rstrip().split()))
        if cmds[0] == 1:
            prfx_sum.append(prfx_sum[-1] + (cmds[1] >= x))
        elif cmds[0] == 3:
            res.append(prfx_sum[p + cmds[1]] - prfx_sum[p])
        else:
            p += 1
    return res


def main():
    n, x = map(int, sys.stdin.readline().rstrip().split())
    prof = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    sys.stdout.write("\n".join(map(str, solution(n, x, prof, m))))


if __name__ == "__main__":
    main()
