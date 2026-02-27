package main

func minFlips(a int, b int, c int) int {
	flips := 0

	for a > 0 || b > 0 || c > 0 {

		bitA := a & 1
		bitB := b & 1
		bitC := c & 1

		bitOR := bitA | bitB
		bitAND := bitA & bitB

		if bitAND == 1 && bitC == 0 {
			flips += 2
		} else if bitOR != bitC {
			flips += 1
		}

		a >>= 1
		b >>= 1
		c >>= 1
	}
	return flips
}
