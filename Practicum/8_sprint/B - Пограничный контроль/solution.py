import sys


def solution(a, b):
    length_a, length_b = len(a), len(b)
    p_a, p_b = 0, 0
    while p_a != length_a and p_b != length_b:
        if a[p_a] != b[p_b]:
            return ["FAIL", "OK"][
                max(
                    a[p_a + 1 :] == b[p_b:],
                    a[p_a:] == b[p_b + 1 :],
                    a[p_a + 1 :] == b[p_b + 1 :],
                )
            ]
        p_a += 1
        p_b += 1
    return "OK"


def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    sys.stdout.write(solution(a, b))


if __name__ == "__main__":
    main()
