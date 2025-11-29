package main

func equalPairs(grid [][]int) int {
	rowsCnt := make(map[[200]int]int)
	row := [200]int{}
	for _, r := range grid {
		copy(row[:], r)
		rowsCnt[row]++
	}
	res := 0
	column := [200]int{}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid); j++ {
			column[j] = grid[j][i]
		}
		res += rowsCnt[column]
	}
	return res
}
