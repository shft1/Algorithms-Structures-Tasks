class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        max_num = 0
        for i in range(k):
            max_num += s[i] in vowels
        window = max_num
        for i in range(k, len(s)):
            window += s[i] in vowels
            window -= s[i - k] in vowels
            max_num = max(max_num, window)
        return max_num
