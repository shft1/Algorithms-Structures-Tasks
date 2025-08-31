package main

import "fmt"

func solution(stocks []int) int {
	profit := 0
	for i := 1; i < len(stocks)-1; i++ {
		if stocks[i-1] >= stocks[i] && stocks[i+1] > stocks[i] {
			profit -= stocks[i]
		} else if stocks[i-1] < stocks[i] && stocks[i+1] <= stocks[i] {
			profit += stocks[i]
		}
	}
	return profit
}

func main() {
	var n, profit int
	fmt.Scan(&n)
	stocks := make([]int, n+2)
	stocks[0], stocks[n+1] = 1001, -1
	for i := 1; i <= n; i++ {
		fmt.Scan(&stocks[i])
	}
	profit = solution(stocks)
	fmt.Println(profit)
}
