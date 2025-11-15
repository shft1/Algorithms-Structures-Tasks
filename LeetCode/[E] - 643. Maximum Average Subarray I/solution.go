package main

func findMaxAverage(nums []int, k int) float64 {
	maxSum := 0
	for i := 0; i < k; i++ {
		maxSum += nums[i]
	}
	windSum := maxSum
	for i := k; i < len(nums); i++ {
		windSum += nums[i]
		windSum -= nums[i-k]
		if windSum > maxSum {
			maxSum = windSum
		}
	}
	return float64(maxSum) / float64(k)
}
