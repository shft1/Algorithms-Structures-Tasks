class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        mx, curr, l = 0, 0, 0
        zero_idx = [-1]
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idx.append(i)
                if k == 0:
                    mx = max(mx, curr)
                    l += 1
                else:
                    k -= 1
            curr = i - zero_idx[l]
        return max(mx, curr)
