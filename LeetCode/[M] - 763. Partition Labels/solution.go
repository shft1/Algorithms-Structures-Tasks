package main

func partitionLabels(s string) []int {
	lstIdx := make(map[rune]int, len(s))
	for i, char := range s {
		lstIdx[char] = i
	}
	var res []int
	var lstGroup int
	var r int
	for l, char := range s {
		r = max(r, lstIdx[char])
		if l == r {
			res = append(res, r-lstGroup+1)
			lstGroup = l + 1
		}
		l++
	}
	return res
}
