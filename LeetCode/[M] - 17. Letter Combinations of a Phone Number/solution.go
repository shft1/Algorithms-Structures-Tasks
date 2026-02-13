package main

func letterCombinations(digits string) []string {
	maps := map[rune]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}
	digts := []rune(digits)
	var res []string

	var fn func([]rune, []rune)

	fn = func(seq, digts []rune) {
		if len(digts) == 0 {
			res = append(res, string(seq))
			return
		}
		for _, char := range maps[digts[0]] {
			seq = append(seq, char)
			fn(seq, digts[1:])
			seq = seq[:len(seq)-1]
		}
	}

	seq := make([]rune, 0, len(digts))
	fn(seq, digts)
	return res
}
