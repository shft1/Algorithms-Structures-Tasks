class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[:k])
        wind_sum = max_sum
        for i in range(k, len(nums)):
            wind_sum += nums[i]
            wind_sum -= nums[i - k]
            max_sum = max(max_sum, wind_sum)
        return max_sum / k
