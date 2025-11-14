package main

func maxOperations(nums []int, k int) int {
	hashCnt := make(map[int]int, len(nums)/2)
	for _, num := range nums {
		hashCnt[num] += 1
	}
	res := 0
	for _, num := range nums {
		find := k - num
		if hashCnt[num] != 0 && hashCnt[find] != 0 {
			if hashCnt[find] > 1 || num != find {
				hashCnt[num]--
				hashCnt[find]--
				res++
			}
		}
	}
	return res
}
