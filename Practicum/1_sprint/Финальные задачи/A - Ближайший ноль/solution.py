import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    houses = list(map(int, sys.stdin.readline().rstrip().split()))
    res = [n] * n
    p = None

    for i in range(n):
        if houses[i] == 0:
            p = i
        if p is None:
            continue
        res[i] = abs(i - p)

    for j in range(p, -1, -1):
        if houses[j] == 0:
            p = j
        res[j] = min(abs(j - p), res[j])

    return ' '.join(map(str, res))

if __name__ == "__main__":
    sys.stdout.write(solution())