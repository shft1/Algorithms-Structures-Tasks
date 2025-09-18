import sys


def main():
    sys.stdout.write(" ".join(sys.stdin.readline().rstrip().split()[::-1]))


if __name__ == "__main__":
    main()
