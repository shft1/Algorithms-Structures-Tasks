import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, x = data[0], data[1]
    arr = data[2:2 + n]
    sorted_arr = sorted(arr)
    mismatches = sum(left != right for left, right in zip(arr, sorted_arr))
    sys.stdout.write("YES" if mismatches <= x else "NO")


if __name__ == "__main__":
    main()
