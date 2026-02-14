package main

func minCostClimbingStairs(cost []int) int {
	dp := make([]int, len(cost))
	prev2, prev1 := cost[0], cost[1]
	for i := 2; i < len(cost); i++ {
		dp[i] = min(prev2, prev1) + cost[i]
		prev2, prev1 = prev1, dp[i]
	}
	return min(prev2, prev1)
}
