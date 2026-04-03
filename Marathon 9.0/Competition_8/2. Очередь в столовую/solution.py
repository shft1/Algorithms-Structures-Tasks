import sys


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        n, d = map(int, sys.stdin.readline().rstrip().split())
        p = 0
        s = [0] * n
        for i in range(n):
            t_i, k_i = map(int, sys.stdin.readline().rstrip().split())
            s[i] = t_i - p
            p += k_i
        sfxMin = [0] * n
        sfxMin[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            sfxMin[i] = min(s[i], sfxMin[i + 1])
        res = n + 1
        for i in range(n):
            if sfxMin[i] >= d:
                res = i + 1
                break
        sys.stdout.write(f"{res}\n")


if __name__ == "__main__":
    main()
