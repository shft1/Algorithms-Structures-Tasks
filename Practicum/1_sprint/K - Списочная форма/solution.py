import sys


def solution():
    len_x = int(sys.stdin.readline().rstrip())
    x_lst = list(map(int, sys.stdin.readline().rstrip().split()))
    k_lst = list(map(int, list(sys.stdin.readline().rstrip())))
    len_k = len(k_lst)
    ost = 0
    res = []

    if len_x > len_k:
        k_lst = [0] * (len_x - len_k) + k_lst
    elif len_k > len_x:
        x_lst = [0] * (len_k - len_x) + x_lst

    start = len(x_lst) - 1

    for i in range(start, -1, -1):
        sumi = x_lst[i] + k_lst[i] + ost
        res.append(str(sumi % 10))
        ost = sumi // 10

    if ost != 0:
        res.append(str(ost))

    sys.stdout.write(" ".join(reversed(res)))


if __name__ == "__main__":
    solution()
