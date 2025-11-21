class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_nums = sum(nums)
        sum_curr = 0
        for i in range(len(nums)):
            if sum_nums - sum_curr - nums[i] == sum_curr:
                return i
            sum_curr += nums[i]
        return -1
