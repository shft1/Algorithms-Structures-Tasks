class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        p1, p2 = 0, 0
        len_w1, len_w2 = len(word1), len(word2)
        choose = 0
        while p1 != len_w1 and p2 != len_w2:
            curr_word = [word1, word2][choose]
            curr_p = [p1, p2][choose]
            res.append(curr_word[curr_p])
            if choose == 0:
                p1 += 1
            else:
                p2 += 1
            choose = (choose + 1) % 2
        if p1 == len_w1:
            res.extend(list(word2[p2:]))
        else:
            res.extend(list(word1[p1:]))
        return "".join(res)
