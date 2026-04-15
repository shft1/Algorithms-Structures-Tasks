from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {char: i for i, char in enumerate(s)}
        res = []
        lastGroup = 0
        l, r = 0, 0
        for l, char in enumerate(s):
            r = max(r, lastIdx[char])
            if l == r:
                res.append(r - lastGroup + 1)
                lastGroup = l + 1
            l += 1
        return res
