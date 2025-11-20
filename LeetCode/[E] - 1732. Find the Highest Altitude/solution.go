package main

func largestAltitude(gain []int) int {
	mxAlt, curr := 0, 0
	for i := 0; i < len(gain); i++ {
		curr += gain[i]
		if curr > mxAlt {
			mxAlt = curr
		}
	}
	return mxAlt
}
