package main

func longestSubarray(nums []int) int {
	mx, curr, l, zIdx := 0, 0, 0, 0
	canDelete := true
	for r := 0; r < len(nums); r++ {
		if nums[r] == 0 && canDelete {
			zIdx = r
			canDelete = false
		} else if nums[r] == 0 && !canDelete {
			mx = max(mx, curr-1)
			l = zIdx + 1
			zIdx = r
		}
		curr = r - l + 1
	}
	return max(mx, curr-1)
}
