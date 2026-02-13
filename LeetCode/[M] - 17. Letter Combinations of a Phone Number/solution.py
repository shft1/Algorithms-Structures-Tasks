from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def combinations(seq, digits):
            if not digits:
                res.append("".join(seq))
                return
            for char in maps[digits[0]]:
                seq.append(char)
                combinations(seq, digits[1:])
                seq.pop()

        combinations([], digits)
        return res
