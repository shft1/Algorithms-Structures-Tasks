import sys


def solution(path):
    lenght_path = len(path)
    dp = [[0, 0] for _ in range(lenght_path)]
    dp[0][1] = 1
    for i in range(1, lenght_path):
        influx = path[i]
        if influx == "L":
            dp[i][0] = min(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
            dp[i][1] = min(dp[i - 1][0] + 2, dp[i - 1][1])
        elif influx == "R":
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + 2)
            dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
        else:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = dp[i - 1][1] + 1
    return dp[lenght_path - 1][1]


def main():
    path = "#" + sys.stdin.readline().rstrip()
    sys.stdout.write(str(solution(path)))


if __name__ == "__main__":
    main()
