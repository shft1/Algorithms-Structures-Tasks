import sys


def solution(n, mushrooms):
    min_V, max_M = float("inf"), -1
    happ_V = 0
    for i in range(n):
        if i % 2 == 0:
            min_V = min(min_V, mushrooms[i])
        else:
            max_M = max(max_M, mushrooms[i])
        happ_V += ((-1) ** i) * mushrooms[i]
    return happ_V + 2 * (max_M - min_V) if min_V < max_M else happ_V


def main():
    n = int(sys.stdin.readline().rstrip())
    mushrooms = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(n, mushrooms)))


if __name__ == "__main__":
    main()
