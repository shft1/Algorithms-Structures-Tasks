package main

func maxVowels(s string, k int) int {
	vows := map[byte]struct{}{
		'a': {},
		'e': {},
		'i': {},
		'o': {},
		'u': {},
	}
	mx := 0
	for i := 0; i < k; i++ {
		if _, ok := vows[s[i]]; ok {
			mx++
		}
	}
	wnd := mx
	for i := k; i < len(s); i++ {
		if _, ok := vows[s[i]]; ok {
			wnd++
		}
		if _, ok := vows[s[i-k]]; ok {
			wnd--
		}
		if wnd > mx {
			mx = wnd
		}
	}
	return mx
}
