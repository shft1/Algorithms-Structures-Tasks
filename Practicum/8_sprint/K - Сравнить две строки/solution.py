import sys


def solution(a, b):
    p_a, p_b = 0, 0
    while p_a != len(a) and p_b != len(b):
        if ord(a[p_a]) % 2 == 0 and ord(b[p_b]) % 2 == 0:
            if a[p_a] < b[p_b]:
                return -1
            if a[p_a] > b[p_b]:
                return 1
        if ord(a[p_a]) % 2 != 0 and ord(b[p_b]) % 2 == 0:
            p_a += 1
        elif ord(a[p_a]) % 2 == 0 and ord(b[p_b]) % 2 != 0:
            p_b += 1
        else:
            p_a += 1
            p_b += 1
    if p_a != len(a):
        for i in range(p_a, len(a)):
            if ord(a[i]) % 2 == 0:
                return 1
    if p_b != len(b):
        for i in range(p_b, len(b)):
            if ord(b[i]) % 2 == 0:
                return -1
    return 0


def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    sys.stdout.write(str(solution(a, b)))


if __name__ == "__main__":
    main()
