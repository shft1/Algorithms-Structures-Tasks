package main

import "slices"

func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string)
	for _, word := range strs {
		bytes := []byte(word)
		slices.Sort(bytes)
		wordS := string(bytes)
		m[wordS] = append(m[wordS], word)
	}
	res := make([][]string, 0, len(m))
	for _, value := range m {
		res = append(res, value)
	}
	return res
}
