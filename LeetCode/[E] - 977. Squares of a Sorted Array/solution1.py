from typing import List

# Counting Sort


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        cntArr = [0] * (max(abs(min(nums)), max(nums)) + 1)
        for num in nums:
            cntArr[abs(num)] += 1
        p = 0
        for i in range(len(cntArr)):
            if cntArr[i] > 0:
                for k in range(cntArr[i]):
                    nums[p] = i * i
                    p += 1
        return nums
