package main

import "slices"

func eraseOverlapIntervals(intervals [][]int) int {
	slices.SortFunc(intervals, func(a, b []int) int {
		return a[1] - b[1]
	})
	cnt := 1
	for i := 1; i < len(intervals); i++ {
		if intervals[i-1][1] <= intervals[i][0] {
			cnt += 1
		} else {
			intervals[i] = intervals[i-1]
		}
	}
	return len(intervals) - cnt
}
