import collections
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, column = len(maze) - 1, len(maze[0]) - 1
        vectors = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        queue = collections.deque([(entrance[0], entrance[1], 0)])
        planned = set((entrance[0], entrance[1]))
        while queue:
            x, y, step = queue.popleft()
            if (
                [x, y] != entrance
                and (x in (0, row) or y in (0, column))
                and maze[x][y] == "."
            ):
                return step
            for dx, dy in vectors:
                xi, yi = x + dx, y + dy
                if (
                    0 <= xi <= row
                    and 0 <= yi <= column
                    and maze[xi][yi] != "+"
                    and (xi, yi) not in planned
                ):
                    queue.append((xi, yi, step + 1))
                    planned.add((xi, yi))
        return -1
