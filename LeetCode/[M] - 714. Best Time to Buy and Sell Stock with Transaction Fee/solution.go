package main

func maxProfit(prices []int, fee int) int {
	hold, cash := 0-prices[0], 0

	for i := 1; i < len(prices); i++ {
		hold, cash = max(hold, cash-prices[i]), max(cash, hold+prices[i]-fee)
	}
	return cash
}
