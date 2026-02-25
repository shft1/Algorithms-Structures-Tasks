package main

func singleNumber(nums []int) int {
	m := make(map[int]int, len(nums))
	for _, num := range nums {
		m[num] += 1
	}
	for k, v := range m {
		if v == 1 {
			return k
		}
	}
	return 0
}
