from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        wind, lay = {}, {}
        for i in range(len(p)):
            wind[s[i]] = wind.get(s[i], 0) + 1
            lay[p[i]] = lay.get(p[i], 0) + 1
        res = []
        if wind == lay:
            res.append(0)
        l = 0
        for r in range(len(p), len(s)):
            wind[s[r]] = wind.get(s[r], 0) + 1
            wind[s[l]] -= 1
            if wind[s[l]] == 0:
                del wind[s[l]]
            l += 1
            if wind == lay:
                res.append(l)
        return res
