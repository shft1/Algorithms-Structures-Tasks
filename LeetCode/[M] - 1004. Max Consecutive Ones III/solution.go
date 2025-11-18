package main

func longestOnes(nums []int, k int) int {
	mx, curr, l := 0, 0, 0
	zeroIdx := make([]int, 0, len(nums))
	zeroIdx = append(zeroIdx, -1)
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			zeroIdx = append(zeroIdx, i)
			if k == 0 {
				if curr > mx {
					mx = curr
				}
				l++
			} else {
				k--
			}
		}
		curr = i - zeroIdx[l]
	}
	return max(mx, curr)
}
