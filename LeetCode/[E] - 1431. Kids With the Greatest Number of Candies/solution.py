class Solution:
    def kidsWithCandies(
        self, candies: list[int], extraCandies: int
    ) -> list[bool]:
        max_cand = max(candies)
        res = []
        for cand in candies:
            res.append([False, True][cand + extraCandies >= max_cand])
        return res
