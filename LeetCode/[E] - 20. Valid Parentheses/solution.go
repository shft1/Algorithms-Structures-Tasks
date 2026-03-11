package main

func isValid(s string) bool {
	m := map[rune]rune{'(': ')', '{': '}', '[': ']'}
	stack := make([]rune, 0)
	for _, r := range s {
		if _, ok := m[r]; ok {
			stack = append(stack, r)
		} else if len(stack) > 0 && m[stack[len(stack)-1]] != 0 && m[stack[len(stack)-1]] == r {
			stack = stack[:len(stack)-1]
		} else {
			return false
		}
	}
	return len(stack) == 0
}
