import sys


def solution(L):
    lenght_L = len(L)
    p = [None] * lenght_L
    p[0] = 0
    for i in range(1, lenght_L):
        k = p[i - 1]
        while k > 0 and L[k] != L[i]:
            k = p[k - 1]
        if L[k] == L[i]:
            k += 1
        p[i] = k
    return " ".join(map(str, p))


def main():
    L = sys.stdin.readline().rstrip()
    sys.stdout.write(solution(L))


if __name__ == "__main__":
    main()
