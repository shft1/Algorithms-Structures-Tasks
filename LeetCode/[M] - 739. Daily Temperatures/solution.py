from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lengthT = len(temperatures)
        stack = [lengthT - 1]
        res = [0] * lengthT

        for i in range(lengthT - 2, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
