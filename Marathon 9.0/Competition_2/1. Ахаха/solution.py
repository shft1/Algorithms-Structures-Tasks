import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    answer = sys.stdin.readline().rstrip()
    maxSeq = 1 if answer[0] in "ah" else 0
    currSeq = 1 if answer[0] in "ah" else 0
    for i in range(1, n):
        curr, prev = answer[i], answer[i - 1]
        if curr == "a" and prev == "h":
            currSeq += 1
        elif curr == "h" and prev == "a":
            currSeq += 1
        else:
            maxSeq = max(maxSeq, currSeq)
            currSeq = 1 if answer[i] in "ah" else 0
    sys.stdout.write(str(max(maxSeq, currSeq)))


if __name__ == "__main__":
    main()
