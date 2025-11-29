class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rowsCnt = {}
        for row in grid:
            row = tuple(row)
            rowsCnt[row] = rowsCnt.get(row, 0) + 1
        res = 0
        for i in range(len(grid)):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            res += rowsCnt.get(tuple(column), 0)
        return res
