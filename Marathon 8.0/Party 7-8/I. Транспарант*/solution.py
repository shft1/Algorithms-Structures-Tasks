import sys


def collect_pairs_d(d):
    pairs = []
    for x in range(int(d**0.5) + 1):
        y2 = d - x * x
        y = int(y2**0.5)
        if y * y == y2:
            pairs.extend([(x, y), (x, -y), (-x, y), (-x, -y)])
    return set(pairs)


def solution(n, d, trees):
    pairs = collect_pairs_d(d)
    cnt = 0
    for x1, y1 in trees:
        for dx, dy in pairs:
            x2, y2 = x1 + dx, y1 + dy
            if (x2, y2) in trees:
                cnt += 1
    return cnt // 2


def main():
    n, d = map(int, sys.stdin.readline().rstrip().split())
    trees = set(
        [
            tuple(map(int, sys.stdin.readline().rstrip().split()))
            for _ in range(n)
        ]
    )
    sys.stdout.write(str(solution(n, d, trees)))


if __name__ == "__main__":
    main()
