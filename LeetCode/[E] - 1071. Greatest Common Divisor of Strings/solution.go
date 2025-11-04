package main

import "strings"

func gcdOfStrings(str1 string, str2 string) string {
	var mnLn int
	if len(str1) > len(str2) {
		mnLn = len(str2)
	} else {
		mnLn = len(str1)
	}
	for i := mnLn; i > 0; i-- {
		if len(str1)%i == 0 && len(str2)%i == 0 {
			cand := str1[:i]
			div1 := strings.Split(str1, cand)
			div2 := strings.Split(str2, cand)
			if strings.Join(div1, "") == "" && strings.Join(div2, "") == "" {
				return cand
			}
		}
	}
	return ""
}
