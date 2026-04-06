from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {}
        sums[0] = 1
        totalSum, res = 0, 0
        for num in nums:
            totalSum += num
            if totalSum - k in sums:
                res += sums[totalSum - k]
            sums[totalSum] = sums.get(totalSum, 0) + 1
        return res
