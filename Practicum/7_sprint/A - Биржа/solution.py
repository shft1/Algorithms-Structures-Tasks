import sys


def solution(n, stocks):
    profit = 0
    for i in range(1, n + 1):
        if stocks[i - 1] > stocks[i] <= stocks[i + 1]:
            profit -= stocks[i]
        elif stocks[i - 1] <= stocks[i] > stocks[i + 1]:
            profit += stocks[i]
    return profit


def main():
    n = int(sys.stdin.readline().rstrip())
    stocks = (
        [float("inf")]
        + list(map(int, sys.stdin.readline().rstrip().split()))
        + [float("-inf")]
    )
    profit = solution(n, stocks)
    sys.stdout.write(str(profit))


if __name__ == "__main__":
    main()
