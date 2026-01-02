package main

func findCircleNum(isConnected [][]int) int {
	cnt, visited := 0, make(map[int]struct{})
	for i := 0; i < len(isConnected); i++ {
		if _, ok := visited[i]; !ok {
			cnt++
			dfs(i, visited, isConnected)
		}
	}
	return cnt
}

func dfs(v int, visited map[int]struct{}, isConnected [][]int) {
	stack := []int{v}
	for len(stack) != 0 {
		v = stack[0]
		stack = stack[1:]
		visited[v] = struct{}{}
		for w := 0; w < len(isConnected[v]); w++ {
			_, ok := visited[w]
			if isConnected[v][w] == 1 && !ok {
				stack = append(stack, w)
			}
		}
	}
}
