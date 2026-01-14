import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, column = len(grid) - 1, len(grid[0]) - 1
        queue = collections.deque()
        for i in range(row + 1):
            for j in range(column + 1):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        minutes = 0
        while queue:
            x, y, m = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xi, yi = x + dx, y + dy
                if 0 <= xi <= row and 0 <= yi <= column and grid[xi][yi] == 1:
                    grid[xi][yi] = 2
                    queue.append((xi, yi, m + 1))
                    minutes = m + 1

        for i in range(row + 1):
            for j in range(column + 1):
                if grid[i][j] == 1:
                    return -1
        return minutes
