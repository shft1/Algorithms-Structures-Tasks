package main

import "slices"

func findMinArrowShots(points [][]int) int {
	slices.SortFunc(points, func(s1, s2 []int) int {
		return s1[1] - s2[1]
	})
	xArr := points[0][1]
	res := 1
	for i := 1; i < len(points); i++ {
		xS, xE := points[i][0], points[i][1]
		if xS > xArr {
			xArr = xE
			res += 1
		}
	}
	return res
}
