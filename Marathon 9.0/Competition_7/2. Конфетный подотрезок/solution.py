import sys
from collections import defaultdict


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = defaultdict(int)
    left, distinct, max_len = 0, 0, 0

    for right in range(n):
        x = arr[right]
        if cnt[x] == 0:
            distinct += 1
        cnt[x] += 1
        while distinct > 2:
            y = arr[left]
            cnt[y] -= 1
            if cnt[y] == 0:
                distinct -= 1
            left += 1
        if distinct == 2:
            max_len = max(max_len, right - left + 1)
    print(max_len)


if __name__ == "__main__":
    main()
