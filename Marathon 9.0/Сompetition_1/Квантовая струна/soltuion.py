import sys


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    events = []
    for _ in range(n):
        l, r, x = map(int, sys.stdin.readline().rstrip().split())
        events.append((l, r, x))
    res = []
    for _ in range(m):
        q = int(sys.stdin.readline().rstrip())
        cur = 0
        for l, r, x in events:
            if l <= q <= r:
                if (q - l) % 2 == 0:
                    cur += x
                else:
                    cur -= x

        res.append(str(cur))

    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    main()
