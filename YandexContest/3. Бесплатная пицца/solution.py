import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    anomalies = []

    for i in range(n):
        diff = arr[(i + 1) % n] - arr[i]
        if diff != 2:
            anomalies.append(i)

    if len(anomalies) == 1:
        k = anomalies[0] + 1
        print(k, k)
    else:
        k = anomalies[0] + 1
        m = anomalies[1] + 1
        if k > m:
            k, m = m, k
        print(k, m)


if __name__ == "__main__":
    main()
