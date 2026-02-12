package main

import "slices"

func minEatingSpeed(piles []int, h int) int {
	l, r := 1, slices.Max(piles)
	k := r
	for l <= r {
		kNew := l + (r-l)/2
		if isValid(kNew, piles, h) {
			k = kNew
			r = kNew - 1
		} else {
			l = kNew + 1
		}
	}
	return k
}

func isValid(kNew int, piles []int, h int) bool {
	hNew := 0
	for _, pile := range piles {
		if pile%kNew == 0 {
			hNew += pile / kNew
		} else {
			hNew += pile/kNew + 1
		}
	}
	return hNew <= h
}
