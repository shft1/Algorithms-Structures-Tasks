package main

func dailyTemperatures(temperatures []int) []int {
	stack := make([]int, 0, len(temperatures))
	stack = append(stack, len(temperatures)-1)
	res := make([]int, len(temperatures))

	for i := len(temperatures) - 2; i > -1; i-- {
		for len(stack) != 0 && temperatures[i] >= temperatures[stack[len(stack)-1]] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			res[i] = 0
		} else {
			res[i] = stack[len(stack)-1] - i
		}
		stack = append(stack, i)
	}
	return res
}
