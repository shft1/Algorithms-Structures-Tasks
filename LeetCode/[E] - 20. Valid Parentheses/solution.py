class Solution:
    def isValid(self, s: str) -> bool:
        m = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for b in s:
            if b in m:
                stack.append(b)
            elif stack and stack[-1] in m and m[stack[-1]] == b:
                stack.pop()
            else:
                return False
        return len(stack) == 0
