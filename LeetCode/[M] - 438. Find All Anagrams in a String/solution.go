package main

import "maps"

func findAnagrams(s string, p string) []int {
	if len(s) < len(p) {
		return nil
	}
	wind, lay := make(map[byte]int, len(p)), make(map[byte]int, len(p))
	for i := range len(p) {
		wind[s[i]]++
		lay[p[i]]++
	}
	var res []int
	if maps.Equal(wind, lay) {
		res = append(res, 0)
	}
	l := 0
	for r := len(p); r < len(s); r++ {
		wind[s[r]]++
		wind[s[l]]--
		if wind[s[l]] == 0 {
			delete(wind, s[l])
		}
		l++
		if maps.Equal(wind, lay) {
			res = append(res, l)
		}
	}
	return res
}
