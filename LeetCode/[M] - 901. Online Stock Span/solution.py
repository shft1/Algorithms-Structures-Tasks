class StockSpanner:
    def __init__(self):
        self.stack = [(-1, 0)]

    def next(self, price: int) -> int:
        days = 1
        while self.stack and price >= self.stack[-1][0]:
            days += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, days))
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
