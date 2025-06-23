import sys


def gen_br_seq(n, seq=[], open_br=0, close_br=0):
    if open_br + close_br == n:
        sys.stdout.write("".join(seq) + "\n")
        return
    if open_br < n // 2:
        seq.append("(")
        gen_br_seq(n, seq, open_br + 1, close_br)
        seq.pop()
    if close_br < open_br:
        seq.append(")")
        gen_br_seq(n, seq, open_br, close_br + 1)
        seq.pop()


def solution():
    n = int(sys.stdin.readline().rstrip())
    gen_br_seq(n * 2)


if __name__ == "__main__":
    solution()
