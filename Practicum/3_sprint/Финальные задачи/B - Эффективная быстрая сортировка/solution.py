import random
import sys


def key(obj):
    return [-obj[1], obj[2], obj[0]]


def partition(arr, lf, rg, pivot):
    lf_up, rg_dwn = lf, rg
    while lf_up <= rg_dwn:
        if key(arr[lf_up]) < key(pivot) <= key(arr[rg_dwn]):
            arr[lf_up], arr[rg_dwn] = arr[rg_dwn], arr[lf_up]
            lf_up += 1
            rg_dwn -= 1
        if key(arr[lf_up]) >= key(pivot):
            lf_up += 1
        if key(arr[rg_dwn]) < key(pivot):
            rg_dwn -= 1
    return rg_dwn, lf_up


def in_place_qsort(arr, lf, rg):
    if lf >= rg:
        return
    pivot = arr[random.randrange(lf, rg + 1)]
    lf_up, rg_dwn = partition(arr, lf, rg, pivot)
    in_place_qsort(arr, lf, lf_up)
    in_place_qsort(arr, rg_dwn, rg)


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = [sys.stdin.readline().rstrip().split() for _ in range(n)]
    for elmnt in arr:
        elmnt[1], elmnt[2] = int(elmnt[1]), int(elmnt[2])

    in_place_qsort(arr, 0, n - 1)

    res = "\n".join([arr[i][0] for i in range(n - 1, -1, -1)])
    sys.stdout.write(res + "\n")
