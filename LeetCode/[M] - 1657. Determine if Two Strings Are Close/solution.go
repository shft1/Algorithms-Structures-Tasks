package main

import "sort"

func closeStrings(word1 string, word2 string) bool {
	seq1, seq2 := make([]int, 26), make([]int, 26)

	for _, ch := range word1 {
		seq1[int(ch)-int('a')] += 1
	}
	for _, ch := range word2 {
		seq2[int(ch)-int('a')] += 1
	}
	for i := 0; i < 26; i++ {
		if (seq1[i] == 0 && seq2[i] != 0) || (seq1[i] != 0 && seq2[i] == 0) {
			return false
		}
	}
	sort.Ints(seq1)
	sort.Ints(seq2)

	for i := 0; i < 26; i++ {
		if seq1[i] != seq2[i] {
			return false
		}
	}
	return true
}
