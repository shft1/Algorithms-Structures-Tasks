package main

func productExceptSelf(nums []int) []int {
	output := make([]int, len(nums))
	output[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		output[i] = output[i-1] * nums[i]
	}
	right := 1
	for j := len(nums) - 1; j > 0; j-- {
		output[j] = output[j-1] * right
		right *= nums[j]
	}
	output[0] = right
	return output
}
