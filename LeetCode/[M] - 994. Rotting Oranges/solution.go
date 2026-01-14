package main

func orangesRotting(grid [][]int) int {
	row, column := len(grid)-1, len(grid[0])-1
	vectors := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	queue := make([][]int, 0)
	for i := 0; i <= row; i++ {
		for j := 0; j <= column; j++ {
			if grid[i][j] == 2 {
				queue = append(queue, []int{i, j, 0})
			}
		}
	}
	minutes := 0
	for len(queue) != 0 {
		x, y, m := queue[0][0], queue[0][1], queue[0][2]
		queue = queue[1:]
		for _, vector := range vectors {
			xi, yi := x+vector[0], y+vector[1]
			if 0 <= xi && xi <= row && 0 <= yi && yi <= column && grid[xi][yi] == 1 {
				grid[xi][yi] = 2
				queue = append(queue, []int{xi, yi, m + 1})
				minutes = m + 1
			}
		}
	}
	for i := 0; i <= row; i++ {
		for j := 0; j <= column; j++ {
			if grid[i][j] == 1 {
				return -1
			}
		}
	}
	return minutes
}
