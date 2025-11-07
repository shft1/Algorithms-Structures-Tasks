class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left].lower() in vowels:
                right -= 1
            elif s[right].lower() in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s)
