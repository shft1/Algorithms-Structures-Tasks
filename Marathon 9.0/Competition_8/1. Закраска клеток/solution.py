import sys


def main():
    conv = {"U": (0, 1), "L": (-1, 0), "D": (0, -1), "R": (1, 0)}
    path = sys.stdin.readline().rstrip()
    curr = (0, 0)
    points = set()
    points.add(curr)
    painted = set()
    res = 0
    for v in path:
        xd, yd = conv[v]
        curr = (curr[0] + xd, curr[1] + yd)
        if curr in points and curr not in painted:
            res += 1
            painted.add(curr)
        else:
            points.add(curr)
    sys.stdout.write(str(res))


if __name__ == "__main__":
    main()
