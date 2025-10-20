import sys


def convert_schedule(n, to):
    sch = []
    for _ in range(n):
        dep, ar = sys.stdin.readline().rstrip().split("-")
        dep_H, dep_M = map(int, dep.split(":"))
        dep = dep_H * 60 + dep_M
        ar_H, ar_M = map(int, ar.split(":"))
        ar = ar_H * 60 + ar_M
        sch.append((dep, to, "s"))
        sch.append((ar, to, "f"))
    return sch


def solution(times):
    cnt_bus = 0
    times.sort(key=lambda x: (x[0], x[2]))
    free = {1: 0, 2: 0}
    for _, vec, cate in times:
        if cate == "s":
            if free[vec]:
                free[vec] -= 1
            else:
                cnt_bus += 1
        else:
            if vec == 1:
                free[2] += 1
            else:
                free[1] += 1
    return cnt_bus


def main():
    times = []
    n = int(sys.stdin.readline().rstrip())
    times.extend(convert_schedule(n, 2))
    m = int(sys.stdin.readline().rstrip())
    times.extend(convert_schedule(m, 1))
    sys.stdout.write(str(solution(times)))


if __name__ == "__main__":
    main()
