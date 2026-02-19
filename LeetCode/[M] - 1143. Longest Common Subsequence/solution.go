package main

func longestCommonSubsequence(text1 string, text2 string) int {
	prev, curr := make([]int, len(text1)+1), make([]int, len(text1)+1)
	for i := 1; i < len(text2)+1; i++ {
		for j := 1; j < len(text1)+1; j++ {
			if text1[j-1] == text2[i-1] {
				curr[j] = prev[j-1] + 1
			} else {
				curr[j] = max(curr[j-1], prev[j])
			}
		}
		prev, curr = curr, make([]int, len(text1)+1)
	}
	return prev[len(prev)-1]
}
