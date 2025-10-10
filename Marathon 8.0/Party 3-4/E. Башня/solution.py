import sys


def solution(n, k, highes):
    if n == k:
        return 1, [1]
    window_sum = sum(highes[1 : k + 1])
    window_min = min(highes[1 : k + 1])
    left = 1
    dp = [0] * (n + 1)
    dp[k] = window_sum * window_min
    prev = [0] * (n + 1)
    for i in range(k + 1, n + 1):
        window_sum += highes[i] - highes[left]
        window_min = min(highes[left + 1 : i + 1])
        dp[i] = max(window_sum * window_min + dp[i - k], dp[i - 1])
        prev[i] = prev[i - 1] if dp[i] == dp[i - 1] else i - k
        left += 1
    res = []
    jump = n
    while dp[jump] != 0:
        jump = prev[jump]
        res.append(jump + 1)
    res.reverse()
    return len(res), res


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    highes = [-1]
    highes.extend(map(int, sys.stdin.readline().rstrip().split()))
    cnt, res = solution(n, k, highes)
    sys.stdout.write(f"{cnt}\n")
    sys.stdout.write(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
