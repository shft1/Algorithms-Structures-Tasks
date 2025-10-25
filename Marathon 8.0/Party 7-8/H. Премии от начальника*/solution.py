import sys


def solution(n, days):
    diff_arr = [0] * n
    for i in range(n - 1):
        sumi = i + days[i]
        if sumi <= i + 1:
            continue
        diff_arr[i + 1] += 1
        if sumi < n:
            diff_arr[sumi] -= 1
    prefix_sum = [0] * n
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + diff_arr[i]
    prize = 0
    for i in range(n):
        prize += prefix_sum[i] * days[i]
    return prize


def main():
    n = int(sys.stdin.readline().rstrip())
    days = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(n, days)))


if __name__ == "__main__":
    main()
