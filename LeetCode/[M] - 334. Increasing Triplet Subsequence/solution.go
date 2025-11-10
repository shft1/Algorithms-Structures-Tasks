package main

import "math"

func increasingTriplet(nums []int) bool {
	smlst1, smlst2 := int(math.Pow(2, 31)), int(math.Pow(2, 31))
	for _, el := range nums {
		switch {
		case el > smlst2:
			return true
		case el > smlst1:
			smlst2 = el
		default:
			smlst1 = el
		}
	}
	return false
}
