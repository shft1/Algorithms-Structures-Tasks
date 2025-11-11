package main

import "strconv"

func compress(chars []byte) int {
	pSymb, pCnt := 0, 0
	cnt := 0
	for pCnt != len(chars) {
		if chars[pSymb] == chars[pCnt] {
			cnt += 1
			pCnt += 1
		} else {
			if cnt < 2 {
				pSymb += 1
				chars[pSymb] = chars[pCnt]
			} else {
				pSymb += 1
				for _, char := range strconv.Itoa(cnt) {
					chars[pSymb] = byte(char)
					pSymb += 1
				}
				chars[pSymb] = chars[pCnt]
			}
			cnt = 0
		}
	}
	if cnt < 2 {
		return pSymb + 1
	}
	pSymb += 1
	for _, char := range strconv.Itoa(cnt) {
		chars[pSymb] = byte(char)
		pSymb += 1
	}
	return pSymb
}
