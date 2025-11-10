class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        smlst1, smlst2 = float("inf"), float("inf")
        for num in nums:
            if num > smlst2:
                return True
            if num > smlst1:
                smlst2 = num
            else:
                smlst1 = num
        return False
