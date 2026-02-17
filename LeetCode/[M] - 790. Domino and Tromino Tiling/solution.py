class Solution:
    def numTilings(self, n: int) -> int:
        FF, F, T, B = 1, 1, 0, 0
        for i in range(2, n + 1):
            FF, F, T, B = F, F + FF + T + B, FF + B, FF + T
        return F % (10**9 + 7)
