package main

func topKFrequent(nums []int, k int) []int {
	m := make(map[int]int, len(nums))
	for _, num := range nums {
		m[num]++
	}

	freqArr := make([][]int, len(nums)+1)
	for key, value := range m {
		freqArr[value] = append(freqArr[value], key)
	}

	res := make([]int, 0, k)

	for i := len(freqArr) - 1; i >= 0 && k != 0; i-- {
		for _, num := range freqArr[i] {
			if k > 0 {
				res = append(res, num)
				k--
			}
		}
	}
	return res
}
