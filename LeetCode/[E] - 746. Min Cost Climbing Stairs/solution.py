from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        prev2, prev1 = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(prev2, prev1) + cost[i]
            prev2, prev1 = prev1, dp[i]

        return min(prev2, prev1)
