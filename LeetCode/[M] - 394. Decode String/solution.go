package main

import (
	"strconv"
	"strings"
)

func reversed(slc []string) []string {
	for i, j := 0, len(slc)-1; i < j; i, j = i+1, j-1 {
		slc[i], slc[j] = slc[j], slc[i]
	}
	return slc
}

func multiSlice(m int, slc []string) []string {
	result := make([]string, 0, len(slc)*m)
	for i := 0; i < m; i++ {
		result = append(result, slc...)
	}
	return result
}

func decodeString(s string) string {
	decode := []string{}
	currentNum := []byte{}
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			currentNum = append(currentNum, s[i])
		} else if s[i] == '[' {
			decode = append(decode, string(currentNum))
			currentNum = []byte{}
		} else if s[i] == ']' {
			letters := []string{}
			for len(decode) > 0 {
				last := decode[len(decode)-1]
				if _, err := strconv.Atoi(last); err == nil {
					break
				}
				letters = append(letters, last)
				decode = decode[:len(decode)-1]
			}
			letters = reversed(letters)
			if len(decode) == 0 {
				decode = append(decode, letters...)
				continue
			}
			m, err := strconv.Atoi(decode[len(decode)-1])
			if err != nil {
				decode = append(decode, letters...)
				continue
			}
			decode = decode[:len(decode)-1]
			repeated := multiSlice(m, letters)
			decode = append(decode, repeated...)

		} else {
			decode = append(decode, string(s[i]))
		}
	}

	return strings.Join(decode, "")
}
