package main

func numTilings(n int) int {
	FF, F, T, B := 1, 1, 0, 0
	for i := 2; i <= n; i++ {
		FF, F, T, B = F, (FF+F+T+B)%1000000007, (FF+B)%1000000007, (FF+T)%1000000007
	}
	return F % 1000000007
}
