package main

func findShortestSubArray(nums []int) int {
	m := make(map[int][]int)
	for i, num := range nums {
		m[num] = append(m[num], i)
	}
	cnt, dist := 0, 0
	for _, v := range m {
		currDist := v[len(v)-1] - v[0] + 1
		if len(v) > cnt {
			cnt = len(v)
			dist = currDist
		} else if len(v) == cnt && currDist < dist {
			dist = currDist
		}
	}
	return dist
}
