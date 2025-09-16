import sys


def solution(n, nums):
    sumi = sum(nums)
    if sumi % 2 != 0:
        return "False"
    weight = sumi // 2
    curr = [0] * (weight + 1)
    prev = [0] * (weight + 1)
    for i in range(n):
        for w in range(1, weight + 1):
            if nums[i] <= w:
                curr[w] = max(nums[i] + prev[w - nums[i]], prev[w])
            else:
                curr[w] = prev[w]
        prev = curr.copy()
        curr = [0] * (weight + 1)
    return "True" if prev[w] == weight else "False"


def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(solution(n, nums))


if __name__ == "__main__":
    main()
