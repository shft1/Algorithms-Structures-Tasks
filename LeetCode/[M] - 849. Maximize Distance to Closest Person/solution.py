from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if len(seats) <= 2:
            return 1
        prfx = [0] * len(seats)
        prfx[0] = 0 if seats[0] == 1 else float("inf")
        for i in range(1, len(seats)):
            if seats[i] == 1:
                prfx[i] = 0
            else:
                prfx[i] = prfx[i - 1] + 1

        maxDist = prfx[-1]

        for j in range(len(seats) - 2, -1, -1):
            if seats[j] == 1:
                prfx[j] = 0
            else:
                prfx[j] = min(prfx[j], prfx[j + 1] + 1)
            maxDist = max(maxDist, prfx[j])
        return maxDist
