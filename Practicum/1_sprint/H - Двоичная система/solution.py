import sys


def solution():
    bin1 = sys.stdin.readline().rstrip()
    bin1_l = len(str(bin1))

    bin2 = sys.stdin.readline().rstrip()
    bin2_l = len(str(bin2))

    accum = 0
    res = []

    if bin1_l > bin2_l:
        bin2 = "0" * (bin1_l - bin2_l) + bin2
    elif bin2_l > bin1_l:
        bin1 = "0" * (bin2_l - bin1_l) + bin1
    start = len(bin1) - 1

    for i in range(start, -1, -1):
        bin1_int = int(bin1[i])
        bin2_int = int(bin2[i])

        if bin1_int + bin2_int + accum == 1:
            res.append("1")
            accum = 0
        elif bin1_int + bin2_int + accum == 2:
            res.append("0")
            accum = 1
        elif bin1_int + bin2_int + accum == 3:
            res.append("1")
            accum = 1
        else:
            res.append("0")
            accum = 0

    if accum == 1:
        res.append("1")

    return "".join(reversed(res))


if __name__ == "__main__":
    sys.stdout.write(solution())
