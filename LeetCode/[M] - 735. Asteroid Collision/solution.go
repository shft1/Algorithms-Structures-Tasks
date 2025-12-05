package main

func asteroidCollision(asteroids []int) []int {
	stack := make([]int, 0)
	for _, a := range asteroids {
		for len(stack) != 0 && (stack[len(stack)-1] > 0 && a < 0) && (stack[len(stack)-1] < -a) {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 || !(stack[len(stack)-1] > 0 && a < 0) {
			stack = append(stack, a)
		} else if stack[len(stack)-1] == -a {
			stack = stack[:len(stack)-1]
		}
	}
	return stack
}
