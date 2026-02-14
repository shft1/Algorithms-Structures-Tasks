package main

func tribonacci(n int) int {
	dp := make([]int, 3+n)
	dp[0], dp[1], dp[2] = 0, 1, 1
	if n < 3 {
		return dp[n]
	}
	for i := 3; i <= n; i++ {
		dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
	}
	return dp[n]
}
