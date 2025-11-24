class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        symb_count = {}
        for num in arr:
            symb_count[num] = symb_count.get(num, 0) + 1
        count_count = {}
        for value in symb_count.values():
            if value in count_count:
                return False
            count_count[value] = 1
        return True
