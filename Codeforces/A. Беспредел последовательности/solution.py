import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    arr = data[1:1 + n]
    sys.stdout.write(str(max(arr) - min(arr)))


if __name__ == "__main__":
    main()
