package main

func countBits(n int) []int {
	dp := make([]int, n+1)
	offset := 1
	for i := 1; i < n+1; i++ {
		if offset*2 == i {
			offset *= 2
		}
		dp[i] = 1 + dp[i-offset]
	}
	return dp
}
