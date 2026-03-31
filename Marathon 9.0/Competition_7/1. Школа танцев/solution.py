import sys
from collections import defaultdict


def main():
    _ = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    prefix = 0
    cnt = defaultdict(int)
    cnt[0] = 1
    ans = 0
    for ch in s:
        if ch == "a":
            prefix += 1
        elif ch == "b":
            prefix -= 1
        ans += cnt[prefix]
        cnt[prefix] += 1
    print(ans)


if __name__ == "__main__":
    main()
