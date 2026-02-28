from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        xArr = points[0][1]
        res = 1
        for i in range(1, len(points)):
            xS, xE = points[i][0], points[i][1]
            if xS > xArr:
                xArr = xE
                res += 1
        return res
