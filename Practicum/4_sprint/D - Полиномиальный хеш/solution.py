import sys


def gorner_polinom_hash(s, a, m):
    hush = 0
    for si in s:
        hush = (hush * a + ord(si)) % m
    return hush


def main():
    a = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    sys.stdout.write(str(gorner_polinom_hash(s, a, m)))


if __name__ == "__main__":
    main()
