import sys


def get_words_by_char(symb, voc):
    left, right = 0, len(voc) - 1
    first_idx = -1
    while left <= right:
        mid = left + (right - left) // 2
        if symb == voc[mid][0]:
            first_idx = mid
            right = mid - 1
        elif symb > voc[mid][0]:
            left = mid + 1
        else:
            right = mid - 1
    res = []
    while first_idx < len(voc) and voc[first_idx][0] == symb:
        res.append(voc[first_idx])
        first_idx += 1
    return res


def solution(string, voc):
    voc.sort()
    length_string = len(string)
    dp = [0] * length_string
    dp[0] = 1
    for i in range(1, length_string):
        if dp[i - 1]:
            words = get_words_by_char(string[i], voc)
            for word in words:
                length_word = len(word)
                if string[i : i + length_word] == word:
                    dp[i + length_word - 1] = length_word
    res = []
    j = length_string - 1
    while j > 0:
        res.append(string[j - dp[j] + 1 : j + 1])
        j -= dp[j]
    res.reverse()
    return " ".join(res)


def main():
    string = "#" + sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    vocabulary = [sys.stdin.readline().rstrip() for _ in range(n)]
    sys.stdout.write(solution(string, vocabulary))


if __name__ == "__main__":
    main()
