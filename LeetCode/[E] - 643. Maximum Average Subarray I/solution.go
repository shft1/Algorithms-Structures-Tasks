package main

func findMaxAverage(nums []int, k int) float64 {
	curr := 0
	for i := 0; i < k; i++ {
		curr += nums[i]
	}
	res := curr
	for r := k; r < len(nums); r++ {
		curr += nums[r] - nums[r-k]
		res = max(res, curr)
	}
	return float64(res) / float64(k)
}
