package main

func firstUniqChar(s string) int {
	m := make(map[rune]int, len(s))
	for _, ch := range s {
		m[ch]++
	}
	for i, ch := range s {
		if m[ch] == 1 {
			return i
		}
	}
	return -1
}
