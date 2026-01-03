package main

func minReorder(n int, connections [][]int) int {
	graph := make(map[int]map[int]struct{})
	order := make(map[int]map[int]struct{})
	for i := 0; i < n; i++ {
		graph[i] = make(map[int]struct{})
		order[i] = make(map[int]struct{})
	}
	for _, conn := range connections {
		x, y := conn[0], conn[1]
		order[x][y] = struct{}{}
		graph[x][y] = struct{}{}
		graph[y][x] = struct{}{}
	}

	cnt := 0

	visited := make(map[int]struct{})
	stack := []int{0}
	for len(stack) != 0 {
		v := stack[0]
		stack = stack[1:]
		visited[v] = struct{}{}
		for w := range graph[v] {
			if _, ok := visited[w]; !ok {
				stack = append(stack, w)
				if _, ok := order[v][w]; ok {
					cnt++
				}
			}
		}
	}
	return cnt
}
