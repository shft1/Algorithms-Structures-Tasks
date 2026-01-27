import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)

        minHeap = []
        curSum = 0
        res = 0

        for n1, n2 in pairs:
            heapq.heappush(minHeap, n1)
            curSum += n1

            if len(minHeap) > k:
                curNum = heapq.heappop(minHeap)
                curSum -= curNum
            if len(minHeap) == k:
                res = max(res, curSum * n2)

        return res
