import sys
from bisect import bisect_left


def solution(x, trains, cars):
    intervals = []
    for a, b, v in trains:
        if a > b:
            v = -v
        t1, t2 = (x - b) / v, (x - a) / v
        intervals.append([t1, t2])
    intervals.sort()
    union = [intervals[0]]
    for s, f in intervals[1:]:
        if s <= union[-1][1]:
            union[-1][1] = max(union[-1][1], f)
        else:
            union.append([s, f])
    res = []
    for t_car in cars:
        EPS = 10 ** (-6)
        indx = bisect_left(union, [t_car])
        if indx == 0:
            if t_car == union[0][0]:
                res.append(union[0][1] + EPS)
            else:
                res.append(t_car)
            continue
        if indx == len(union):
            if t_car <= union[-1][1]:
                res.append(union[-1][1] + EPS)
            else:
                res.append(t_car)
            continue
        if union[indx - 1][1] < t_car < union[indx][0]:
            res.append(t_car)
        elif t_car < union[indx][0] and t_car <= union[indx - 1][1]:
            res.append(union[indx - 1][1] + EPS)
        elif union[indx][0] <= t_car <= union[indx][1]:
            res.append(union[indx][1] + EPS)
    return res


def main():
    n, m, x = map(int, sys.stdin.readline().split())
    trains = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    cars = list(map(int, sys.stdin.readline().split()))
    ans = solution(x, trains, cars)
    sys.stdout.write("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
