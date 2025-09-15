import sys


def solution(s, t):
    l_s, l_t = len(s), len(t)
    curr = [float("inf") for _ in range(l_t + 1)]
    prev = [j for j in range(l_t, -1, -1)]

    for i in range(l_s - 1, -1, -1):
        curr[-1] = l_s - i
        for j in range(l_t - 1, -1, -1):
            if s[i] == t[j]:
                curr[j] = prev[j + 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j + 1], prev[j + 1])
        prev = curr.copy()
        curr = [float("inf") for _ in range(l_t + 1)]

    return prev[0]


def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    sys.stdout.write(str(solution(s, t)))


if __name__ == "__main__":
    main()
