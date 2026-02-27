class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            bit_or = bit_a | bit_b
            bit_and = bit_a & bit_b

            if bit_and == 1 and bit_c == 0:
                flips += 2
            elif bit_or != bit_c:
                flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
