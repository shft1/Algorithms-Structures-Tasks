package main

func isSubsequence(s string, t string) bool {
	ps, pt := 0, 0
	for ps < len(s) && pt < len(t) {
		if s[ps] == t[pt] {
			ps++
		}
		pt++
	}
	return ps == len(s)
}
