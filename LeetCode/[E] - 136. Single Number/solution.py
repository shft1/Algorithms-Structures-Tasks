from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = 1 + m[num] if num in m else 1
        for key, value in m.items():
            if value == 1:
                return key
