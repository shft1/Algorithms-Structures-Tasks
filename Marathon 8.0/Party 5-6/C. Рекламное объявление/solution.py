import sys


def is_good_k(W, H, def_wind, k):
    prev_W = def_wind[0][0] * k
    prev_H = def_wind[0][1] * k
    if not (prev_W <= W and prev_H <= H):
        return False
    left_W, left_H = W - prev_W, H - prev_H
    for i in range(1, len(def_wind)):
        check_W = def_wind[i][0] * k
        check_H = def_wind[i][1] * k
        if check_H == prev_H and check_W <= left_W:
            left_W -= check_W
        else:
            if check_H <= left_H and check_W <= W:
                left_H -= check_H
                left_W = W - check_W
                prev_W, prev_H = check_W, check_H
            else:
                return False
    return True


def solution(N, W, H, EPS, def_wind):
    left, right = 0, W + 1
    while right - left > EPS:
        check_k = left + (right - left) / 2
        if is_good_k(W, H, def_wind, check_k):
            left = check_k
        else:
            right = check_k
    return left


def main():
    N, W, H = map(int, sys.stdin.readline().rstrip().split())
    def_wind = [
        tuple(map(int, sys.stdin.readline().rstrip().split()))
        for _ in range(N)
    ]
    EPS = 10 ** (-6)
    sys.stdout.write(str(solution(N, W, H, EPS, def_wind)))


if __name__ == "__main__":
    main()
