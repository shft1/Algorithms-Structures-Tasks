package main

func pivotIndex(nums []int) int {
	sumNum := 0
	for _, el := range nums {
		sumNum += el
	}
	sumCurr := 0
	for i := 0; i < len(nums); i++ {
		if sumNum-sumCurr-nums[i] == sumCurr {
			return i
		}
		sumCurr += nums[i]
	}
	return -1
}
