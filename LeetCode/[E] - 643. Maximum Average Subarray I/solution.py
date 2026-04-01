from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind = sum(nums[:k])
        res = wind
        l = 0
        for r in range(k, len(nums)):
            wind += nums[r] - nums[l]
            res = max(res, wind)
            l += 1
        return res / k
