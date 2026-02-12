from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = right
        while left <= right:
            kNew = left + (right - left) // 2
            if self.isValid(kNew, piles, h):
                k = kNew
                right = kNew - 1
            else:
                left = kNew + 1
        return k

    def isValid(self, kNew, piles, h):
        hNew = 0
        for pile in piles:
            hNew += (pile // kNew) + (pile % kNew != 0)
        return hNew <= h
