package main

func mergeAlternately(word1 string, word2 string) string {
	var (
		p1 int
		p2 int
	)
	res := make([]byte, 0, len(word1)+len(word2))
	ch := 0
	wrds := []string{word1, word2}
	pnts := []*int{&p1, &p2}
	for p1 != len(word1) && p2 != len(word2) {
		curr_wrd := wrds[ch]
		curr_pnt := pnts[ch]
		res = append(res, curr_wrd[*curr_pnt])
		if ch == 0 {
			p1 += 1
		} else {
			p2 += 1
		}
		ch = (ch + 1) % 2
	}
	if p1 == len(word1) {
		for p2 != len(word2) {
			res = append(res, word2[p2])
			p2 += 1
		}
	} else {
		for p1 != len(word1) {
			res = append(res, word1[p1])
			p1 += 1
		}
	}
	return string(res)
}
