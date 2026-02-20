from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, cash = 0 - prices[0], 0

        for i in range(1, len(prices)):
            hold, cash = (
                max(hold, cash - prices[i]),
                max(cash, hold + prices[i] - fee),
            )

        return cash
