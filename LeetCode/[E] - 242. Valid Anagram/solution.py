class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for char in s:
            sMap[char] = sMap.get(char, 0) + 1
        for char in t:
            if char not in sMap:
                return False
            sMap[char] -= 1
        for cnt in sMap.values():
            if cnt < 0 or cnt > 0:
                return False
        return True
