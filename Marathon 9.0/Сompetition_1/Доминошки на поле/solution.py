import sys


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    field = [["#" for _ in range(m + 2)]]
    for _ in range(n):
        field.append(["#"] + list(sys.stdin.readline().rstrip()) + ["#"])
    field.append(["#" for _ in range(m + 2)])

    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if field[i][j] == "#":
                continue
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if field[i + x][j + y] != "#":
                    res += 1
            field[i][j] = "#"
    sys.stdout.write(str(res))


if __name__ == "__main__":
    main()
