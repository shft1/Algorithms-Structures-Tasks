import sys


def solution(a, b, S):
    f, g, z = -a + (-b), 1, a * b - S
    D = f**2 - 4 * g * z
    x1 = (-f + D**0.5) / (2 * g)
    x2 = (-f - D**0.5) / (2 * g)
    if x1 > 0 and int(x1) == x1:
        return int(x1)
    if x2 > 0 and int(x2) == x2:
        return int(x2)
    return -1


def main():
    a, b, S = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(a, b, S)))


if __name__ == "__main__":
    main()
