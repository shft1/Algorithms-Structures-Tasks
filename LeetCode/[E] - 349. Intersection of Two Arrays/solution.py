from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l, r = 0, 0
        lenNums1, lenNums2 = len(nums1), len(nums2)
        used = set()
        res = []
        while l < lenNums1 and r < lenNums2:
            if nums1[l] == nums2[r]:
                if nums1[l] not in used:
                    res.append(nums1[l])
                    used.add(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return res
