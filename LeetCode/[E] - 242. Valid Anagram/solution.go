package main

func isAnagram(s string, t string) bool {
	sMap := make(map[rune]int)
	for _, r := range s {
		sMap[r] += 1
	}
	for _, r := range t {
		if _, ok := sMap[r]; !ok {
			return false
		}
		sMap[r]--
	}
	for _, value := range sMap {
		if value < 0 || value > 0 {
			return false
		}
	}
	return true
}
