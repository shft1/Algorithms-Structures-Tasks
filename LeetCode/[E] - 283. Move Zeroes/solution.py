class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        p_zero = 0
        for p_value in range(len(nums)):
            if nums[p_value] != 0:
                nums[p_zero], nums[p_value] = nums[p_value], nums[p_zero]
                p_zero += 1
