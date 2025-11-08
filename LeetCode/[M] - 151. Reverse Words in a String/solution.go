package main

import "strings"

func reverseWords(s string) string {
	slce := strings.Fields(s)
	for i, j := 0, len(slce)-1; i < j; i, j = i+1, j-1 {
		slce[i], slce[j] = slce[j], slce[i]
	}
	return strings.Join(slce, " ")
}
