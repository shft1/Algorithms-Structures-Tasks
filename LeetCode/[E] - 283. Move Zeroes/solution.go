package main

func moveZeroes(nums []int) {
	pZero := 0
	for pValue := 0; pValue < len(nums); pValue++ {
		if nums[pValue] != 0 {
			nums[pValue], nums[pZero] = nums[pZero], nums[pValue]
			pZero++
		}
	}
}
