package main

func removeDuplicates(nums []int) int {
	ins := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != nums[ins] {
			ins++
			nums[ins] = nums[i]
		}
	}
	return ins + 1
}
