import sys


INF = 10**18


class SegmentTree:
    def __init__(self, n: int) -> None:
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.data = [INF] * (2 * size)

    def update(self, pos: int, value: int) -> None:
        pos += self.size
        self.data[pos] = value
        pos >>= 1
        while pos:
            self.data[pos] = min(self.data[pos << 1], self.data[pos << 1 | 1])
            pos >>= 1

    def query(self, left: int, right: int) -> int:
        left += self.size
        right += self.size
        result = INF
        while left <= right:
            if left & 1:
                result = min(result, self.data[left])
                left += 1
            if not (right & 1):
                result = min(result, self.data[right])
                right -= 1
            left >>= 1
            right >>= 1
        return result


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]
    dp = [0] * n
    tree = SegmentTree(n)
    answer = 0

    for i in range(n):
        if a[i] >= i + 1:
            dp[i] = 1
        else:
            left = i - a[i]
            right = i - 1
            dp[i] = 1 + tree.query(left, right)

        tree.update(i, dp[i])
        answer += dp[i]

    sys.stdout.write(str(answer))


if __name__ == "__main__":
    main()
