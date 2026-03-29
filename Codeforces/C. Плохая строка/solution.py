import sys


def main() -> None:
    s = sys.stdin.read().strip()
    if not s:
        return
    sys.stdout.write(s[::-1])


if __name__ == "__main__":
    main()
