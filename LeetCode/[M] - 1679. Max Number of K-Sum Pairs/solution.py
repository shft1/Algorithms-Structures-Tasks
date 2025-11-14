class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        hash_count = {}
        for num in nums:
            hash_count[num] = hash_count.get(num, 0) + 1
        res = 0
        for num in nums:
            find = k - num
            if hash_count[num] and hash_count.get(find, 0):
                if hash_count[find] > 1 or num != find:
                    hash_count[find] -= 1
                    hash_count[num] -= 1
                    res += 1
        return res
