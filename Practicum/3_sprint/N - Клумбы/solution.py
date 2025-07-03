import sys


def solution():
    """
    Time: O(nlogn)
    Mem: O(1)
    """
    n = int(sys.stdin.readline().rstrip())
    sgmts_arr = [
        list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)
    ]
    sgmts_arr.sort()
    main_idx, cand_idx = 0, 0
    while cand_idx != n:
        main = sgmts_arr[main_idx]
        candidate = sgmts_arr[cand_idx]
        if main[1] >= candidate[0]:
            if candidate[1] > main[1]:
                main[1] = candidate[1]
        else:
            sys.stdout.write(" ".join(map(str, main)) + "\n")
            main_idx = cand_idx
        cand_idx += 1

    sys.stdout.write(" ".join(map(str, sgmts_arr[main_idx])) + "\n")


if __name__ == "__main__":
    solution()
