package main

type StockSpanner struct {
	stack [][]int
}

func Constructor() StockSpanner {
	return StockSpanner{stack: make([][]int, 0)}
}

func (ss *StockSpanner) Next(price int) int {
	days := 1
	for len(ss.stack) != 0 && price >= ss.stack[len(ss.stack)-1][0] {
		days += ss.stack[len(ss.stack)-1][1]
		ss.stack = ss.stack[:len(ss.stack)-1]
	}
	ss.stack = append(ss.stack, []int{price, days})
	return days
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
