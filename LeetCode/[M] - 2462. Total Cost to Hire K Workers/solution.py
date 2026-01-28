import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        right = candidates - 1
        heap1 = costs[: right + 1]
        heapq.heapify(heap1)

        left = max(right + 1, len(costs) - candidates)
        heap2 = costs[len(costs) - 1 : left - 1 : -1]
        heapq.heapify(heap2)

        res = 0

        l1, l2 = len(heap1), len(heap2)
        while k != 0 and l1 != 0 and l2 != 0:
            if heap1[0] <= heap2[0]:
                res += heapq.heappop(heap1)
                k -= 1
                l1 -= 1
                if right + 1 < left:
                    right += 1
                    heapq.heappush(heap1, costs[right])
                    l1 += 1
            else:
                res += heapq.heappop(heap2)
                k -= 1
                l2 -= 1
                if left - 1 > right:
                    left -= 1
                    heapq.heappush(heap2, costs[left])
                    l2 += 1

        while k != 0 and l1 != 0:
            res += heapq.heappop(heap1)
            k -= 1
            l1 -= 1

        while k != 0 and l2 != 0:
            res += heapq.heappop(heap2)
            k -= 1
            l2 -= 1

        return res
