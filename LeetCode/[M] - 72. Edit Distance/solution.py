class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l_s, l_t = len(word1), len(word2)
        curr = [float("inf") for _ in range(l_t + 1)]
        prev = [j for j in range(l_t, -1, -1)]

        for i in range(l_s - 1, -1, -1):
            curr[-1] = l_s - i
            for j in range(l_t - 1, -1, -1):
                if word1[i] == word2[j]:
                    curr[j] = prev[j + 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j + 1], prev[j + 1])
            prev = curr.copy()
            curr = [float("inf") for _ in range(l_t + 1)]

        return prev[0]
