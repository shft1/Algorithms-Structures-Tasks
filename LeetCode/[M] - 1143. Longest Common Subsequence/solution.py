class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev, curr = [0] * (len(text1) + 1), [0] * (len(text1) + 1)

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev, curr = curr, [0] * (len(text1) + 1)

        return prev[-1]
