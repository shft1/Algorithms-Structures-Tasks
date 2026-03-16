package main

import "maps"

func findAnagrams(s string, p string) []int {
	if len(p) > len(s) {
		return []int{}
	}
	pattern := make(map[byte]int, len(p))
	for i := range p {
		pattern[p[i]] += 1
	}
	src := make(map[byte]int)
	for r := 0; r < len(p); r++ {
		src[s[r]] += 1
	}
	var res []int
	if maps.Equal(src, pattern) {
		res = append(res, 0)
	}
	l := 0
	for r := len(p); r < len(s); r++ {
		src[s[r]] += 1
		src[s[l]] -= 1
		if src[s[l]] == 0 {
			delete(src, s[l])
		}
		l++
		if maps.Equal(src, pattern) {
			res = append(res, l)
		}
	}
	return res
}
