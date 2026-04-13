package main

// Two pointers

func sortedSquares(nums []int) []int {
	l, r := 0, len(nums)-1
	p := len(nums) - 1
	res := make([]int, len(nums))
	for p >= 0 {
		if IntAbs(nums[l]) > IntAbs(nums[r]) {
			res[p] = nums[l] * nums[l]
			l++
		} else {
			res[p] = nums[r] * nums[r]
			r--
		}
		p--
	}
	return res
}

func IntAbs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
