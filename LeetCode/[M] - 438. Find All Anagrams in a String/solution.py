from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pattern = defaultdict(int)
        for c in p:
            pattern[c] += 1

        src = defaultdict(int)
        for r in range(len(p)):
            src[s[r]] += 1

        l = 0

        res = []
        if src == pattern:
            res.append(l)

        for r in range(len(p), len(s)):
            src[s[r]] += 1
            src[s[l]] -= 1
            if src[s[l]] == 0:
                del src[s[l]]
            l += 1
            if src == pattern:
                res.append(l)

        return res
