class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        output = [nums[0]] * len_nums
        for i in range(1, len_nums):
            output[i] = output[i - 1] * nums[i]
        product_r = 1
        for j in range(len_nums - 1, 0, -1):
            output[j] = output[j - 1] * product_r
            product_r *= nums[j]
        output[0] = product_r
        return output
