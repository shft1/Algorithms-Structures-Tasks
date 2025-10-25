import sys


def solution(n, series, koeff):
    pairs = [(series[i], koeff[i]) for i in range(n)]
    pairs.sort()
    sum_koeff = sum(koeff)
    median = sum_koeff / 2
    curr_sum_koeff = 0
    res_e = None
    for e, k in pairs:
        curr_sum_koeff += k
        if curr_sum_koeff >= median:
            res_e = e
            break
    res_k = 0
    for e, k in pairs:
        res_k += abs(e - res_e) * k
    return res_e, res_k


def main():
    n = int(sys.stdin.readline().rstrip())
    series = list(map(int, sys.stdin.readline().rstrip().split()))
    koeff = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(" ".join(map(str, solution(n, series, koeff))))


if __name__ == "__main__":
    main()
