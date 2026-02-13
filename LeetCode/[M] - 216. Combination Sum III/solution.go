package main

func combinationSum3(k int, n int) [][]int {
	var res [][]int
	var fn func(int, []int)

	fn = func(x int, seq []int) {
		if len(seq) == k {
			if sliceSum(seq) == n {
				tmp := make([]int, len(seq))
				copy(tmp, seq)
				res = append(res, tmp)
			}
			return
		}
		if sliceSum(seq) > n {
			return
		}

		for i := x; i < 10; i++ {
			seq = append(seq, i)
			fn(i+1, seq)
			seq = seq[:len(seq)-1]
		}
	}

	fn(1, []int(nil))

	return res
}

func sliceSum(slice []int) int {
	sum := 0
	for _, num := range slice {
		sum += num
	}
	return sum
}
