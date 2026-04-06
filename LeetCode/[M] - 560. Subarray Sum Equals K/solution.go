package main

func subarraySum(nums []int, k int) int {
	m := make(map[int]int)
	m[0] = 1
	sum := 0
	res := 0
	for _, num := range nums {
		sum += num
		if cnt, ok := m[sum-k]; ok {
			res += cnt
		}
		m[sum]++
	}
	return res
}
