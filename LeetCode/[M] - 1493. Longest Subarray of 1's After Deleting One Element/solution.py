class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        mx, curr, l, zdx = 0, 0, 0, -1
        can_delete = True
        for r in range(len(nums)):
            if nums[r] == 0 and can_delete:
                zdx = r
                can_delete = False
            elif nums[r] == 0 and not can_delete:
                mx = max(mx, curr - 1)
                l = zdx + 1
                zdx = r
            curr = r - l + 1
        return max(mx, curr - 1)
