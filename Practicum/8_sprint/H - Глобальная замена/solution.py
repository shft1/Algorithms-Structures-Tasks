import sys


def solution(text: str, s: str, t: str) -> str:
    lenght_s = len(s)
    comb_txt = s + "#" + text
    res = []
    pFs = [0] + [None] * (lenght_s - 1)
    prev_pF = 0
    for i in range(1, len(comb_txt)):
        k = prev_pF
        while k > 0 and comb_txt[k] != comb_txt[i]:
            k = pFs[k - 1]
        if comb_txt[k] == comb_txt[i]:
            k += 1
        if i < lenght_s:
            pFs[i] = k
        prev_pF = k
        if i >= lenght_s + 1:
            res.append(comb_txt[i])
        if k == lenght_s:
            res[-lenght_s::] = list(t)
    return "".join(res)


def main():
    text = sys.stdin.readline().rstrip()
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    sys.stdout.write(solution(text, s, t))


if __name__ == "__main__":
    main()
