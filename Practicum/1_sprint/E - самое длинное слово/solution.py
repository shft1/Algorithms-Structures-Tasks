import sys


def solution():
    sent_l = int(sys.stdin.readline().rstrip())
    sent = sys.stdin.readline().strip().split()

    res_word = ''
    res_l = 0

    for word in sent:
        word_l = len(word)
        if word_l > res_l:
            res_l = word_l
            res_word = word

    return res_word, res_l


if __name__ == "__main__":
    mx_string, mx_len = solution()
    sys.stdout.write(mx_string + '\n')
    sys.stdout.write(str(mx_len))
