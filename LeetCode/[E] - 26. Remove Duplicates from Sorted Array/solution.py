from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ins = 0
        for num in nums:
            if num != nums[ins]:
                ins += 1
                nums[ins] = num
        return ins + 1
