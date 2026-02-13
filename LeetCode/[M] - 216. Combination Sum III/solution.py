from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtracking(i, seq):
            if len(seq) == k:
                if sum(seq) == n:
                    res.append(seq)
                return
            if sum(seq) > n:
                return

            for x in range(i, 10):
                backtracking(x + 1, seq + [x])

        backtracking(1, [])
        return res
