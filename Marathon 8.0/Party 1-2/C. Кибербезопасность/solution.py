import sys


def solution(s):
    length_s = len(s)
    cnt = {}
    for char in s:
        cnt[char] = cnt.get(char, 0) + 1
    res = 0
    for value in cnt.values():
        res += (length_s - value) * value
    return 1 + res // 2


def main():
    s = sys.stdin.readline().rstrip()
    sys.stdout.write(str(solution(s)))


if __name__ == "__main__":
    main()
