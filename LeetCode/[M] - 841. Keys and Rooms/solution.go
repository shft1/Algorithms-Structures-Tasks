package main

func canVisitAllRooms(rooms [][]int) bool {
	marked := make(map[int]struct{})
	marked[0] = struct{}{}
	stack := []int{0}
	for len(stack) != 0 {
		v := stack[0]
		stack = stack[1:]
		for _, w := range rooms[v] {
			if _, ok := marked[w]; !ok {
				stack = append(stack, w)
				marked[w] = struct{}{}
			}
		}
	}
	return len(marked) == len(rooms)
}
