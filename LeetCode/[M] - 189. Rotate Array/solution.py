from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        lenNums = len(nums)
        i, j = lenNums - (k % lenNums), len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        i, j = 0, lenNums - (k % lenNums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        i, j = 0, lenNums - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
