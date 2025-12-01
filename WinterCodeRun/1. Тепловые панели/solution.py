import sys


def main():
    R, B = map(int, sys.stdin.readline().rstrip().split())
    sumBR = B + R
    d = 1
    for h in range(2, int(sumBR ** 0.5) + 1):
        if sumBR % h == 0 and ((h - 2) * (sumBR // h - 2)) == B:
            d = h
    sys.stdout.write(f"{sumBR // d} {d}")


if __name__ == '__main__':
    main()
