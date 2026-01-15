from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            pivot, p, cnt = nums[r], l, 0
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    if nums[i] == pivot:
                        cnt += 1
            nums[p], nums[r] = nums[r], nums[p]
            if k < p - cnt:
                return quick_select(l, p - 1)
            elif k > p:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)
