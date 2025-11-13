package main

func maxArea(height []int) int {
	l, r := 0, len(height)-1
	maxArea := 0
	for l < r {
		h := min(height[l], height[r])
		area := (r - l) * h
		if area > maxArea {
			maxArea = area
		}
		if height[l] <= height[r] {
			l++
		} else {
			r--
		}
	}
	return maxArea
}
