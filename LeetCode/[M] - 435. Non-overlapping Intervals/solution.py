from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] <= intervals[i][0]:
                cnt += 1
            else:
                intervals[i] = intervals[i - 1]
        return len(intervals) - cnt
