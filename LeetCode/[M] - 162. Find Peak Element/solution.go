package main

func findPeakElement(nums []int) int {
	l, r := 0, len(nums)-1
	var res int
	for l <= r {
		m := l + (r-l)/2
		if m > 0 && nums[m] < nums[m-1] {
			r = m - 1
		} else if m < len(nums)-1 && nums[m] < nums[m+1] {
			l = m + 1
		} else {
			res = m
			break
		}
	}
	return res
}
