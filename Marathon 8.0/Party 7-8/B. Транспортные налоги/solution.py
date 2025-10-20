import sys
from bisect import bisect_left


def solution(m, table):
    sort_keys = list(table.keys())
    res = []
    for _ in range(m):
        curr_power = int(sys.stdin.readline().rstrip())
        idx = bisect_left(sort_keys, curr_power)
        res.append(curr_power * table[sort_keys[idx - 1]])
    return res


def main():
    n = int(sys.stdin.readline().rstrip())
    table = {}
    for _ in range(n):
        power, rate = map(int, sys.stdin.readline().rstrip().split())
        table[power] = rate
    m = int(sys.stdin.readline().rstrip())
    sys.stdout.write("\n".join(map(str, solution(m, table))))


if __name__ == "__main__":
    main()
